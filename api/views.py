from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from django.http import JsonResponse
from .models import User, Blog
from .serializers import BlogSerializer
import requests
import os

# ✅ Home View
def home(request):
    return JsonResponse({"message": "Welcome to the Blog Generator API!"})

# ✅ Fixed Registration API (Now Properly Hashes Password)
class RegisterAPIView(APIView):
    permission_classes = [AllowAny]  # Allow anyone to register

    def post(self, request):
        username = request.data.get("username")
        email = request.data.get("email")
        password = request.data.get("password")
        confirm_password = request.data.get("confirm_password")

        if not username or not email or not password or not confirm_password:
            return Response({"error": "All fields are required"}, status=400)

        if password != confirm_password:
            return Response({"error": "Passwords do not match"}, status=400)

        if User.objects.filter(username=username).exists():
            return Response({"error": "Username already taken"}, status=400)

        user = User(username=username, email=email)
        user.set_password(password)  # ✅ Fix: Hash the password properly
        user.save()

        refresh = RefreshToken.for_user(user)
        return Response({"message": "User registered successfully", "token": str(refresh.access_token)}, status=201)

# ✅ Fixed Login API (Properly Authenticates Users)
class LoginAPIView(APIView):
    permission_classes = [AllowAny]  # Allow anyone to log in

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        if not username or not password:
            return Response({"error": "Both username and password are required"}, status=400)

        # Fetch user from database
        user = User.objects.filter(username=username).first()

        # Check if user exists and password is correct
        if user and user.check_password(password):  # ✅ Ensure correct password check
            refresh = RefreshToken.for_user(user)
            return Response({
                "message": "Login successful",
                "token": str(refresh.access_token),
                "username": user.username
            }, status=200)

        return Response({"error": "Invalid credentials"}, status=401)

# ✅ Fixed Blog Generation API (Now Works with LLaMA & Hugging Face API)
class BlogGenerateAPIView(APIView):
    permission_classes = [IsAuthenticated]  # ✅ User must be logged in

    def post(self, request):
        title = request.data.get("title")
        audience = request.data.get("audience")
        word_count = request.data.get("word_count")

        if not title or not audience or not word_count:
            return Response({"error": "All fields are required"}, status=400)

        prompt = f"Write a {word_count}-word blog for {audience} about {title}."

        # ✅ Use Local LLaMA Model
        MODEL_PATH = "models/llama-2-7b-chat.Q4_K_M.gguf"
        try:
            from langchain_community.llms import CTransformers

            llm = CTransformers(
                model=MODEL_PATH,
                model_type="llama",
                config={
                    "max_new_tokens": 100,
                    "temperature": 0.3,
                    "context_length": 256,
                    "batch_size": 4,
                }
            )
            blog_content = llm.invoke(prompt)

        except Exception as e:
            # ✅ Fallback to Hugging Face API if Local Model Fails
            HF_API_URL = "https://api-inference.huggingface.co/models/meta-llama/Llama-2-7b-chat-hf"
            headers = {"Authorization": f"Bearer {os.getenv('HUGGINGFACE_API_KEY')}"}
            response = requests.post(HF_API_URL, json={"inputs": prompt}, headers=headers)

            if response.status_code == 200:
                result = response.json()
                blog_content = result[0].get("generated_text", "No content generated.") if isinstance(result, list) else "Error: No valid response."
            else:
                return Response({"error": "Model error"}, status=500)

        return Response({"blog_content": blog_content}, status=200)

# ✅ Fixed Save Blog API (Now Saves to MySQL)
class SaveBlogAPIView(APIView):
    permission_classes = [IsAuthenticated]  # ✅ User must be logged in

    def post(self, request):
        title = request.data.get("title")
        content = request.data.get("content")

        if not title or not content:
            return Response({"error": "Title and content are required"}, status=400)

        # ✅ Fix: Use request.user as the author
        blog = Blog.objects.create(title=title, content=content, author=request.user)
        return Response(BlogSerializer(blog).data, status=201)

# ✅ Fixed Blog History API (Fetches User’s Saved Blogs)
class BlogHistoryAPIView(APIView):
    permission_classes = [IsAuthenticated]  # ✅ User must be logged in

    def get(self, request):
        blogs = Blog.objects.filter(author=request.user)  # ✅ Fix: Filter by logged-in user
        return Response(BlogSerializer(blogs, many=True).data, status=200)
