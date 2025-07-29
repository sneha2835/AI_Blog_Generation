# api/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from django.http import JsonResponse
from django.conf import settings
from .models import User, Blog
from .serializers import BlogSerializer
import os
from .utils.model_loader import load_llama_model
# ----------------- Load LLaMA Model Once -----------------
llm = load_llama_model()

# ----------------- Simple Home -----------------
def home(request):
    return JsonResponse({"message": "Welcome to the Blog Generator API!"})

# ----------------- Register -----------------
class RegisterAPIView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        username = request.data.get("username")
        email = request.data.get("email")
        password = request.data.get("password")
        confirm_password = request.data.get("confirm_password")

        if not all([username, email, password, confirm_password]):
            return Response({"error": "All fields are required"}, status=400)
        if password != confirm_password:
            return Response({"error": "Passwords do not match"}, status=400)
        if User.objects.filter(username=username).exists():
            return Response({"error": "Username already taken"}, status=400)

        user = User(username=username, email=email)
        user.set_password(password)
        user.save()

        refresh = RefreshToken.for_user(user)
        return Response({"message": "User registered successfully", "token": str(refresh.access_token)}, status=201)

# ----------------- Login -----------------
class LoginAPIView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        if not username or not password:
            return Response({"error": "Both username and password are required"}, status=400)

        user = User.objects.filter(username=username).first()
        if user and user.check_password(password):
            refresh = RefreshToken.for_user(user)
            return Response({
                "message": "Login successful",
                "token": str(refresh.access_token),
                "username": user.username
            }, status=200)
        return Response({"error": "Invalid username or password."}, status=401)

# ----------------- Blog Generation (Local Model) -----------------
class BlogGenerateAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        title = request.data.get("title")
        audience = request.data.get("audience")
        word_count = request.data.get("word_count")

        if not all([title, audience, word_count]):
            return Response({"error": "All fields are required"}, status=400)

        prompt = f"Write a {word_count}-word blog for {audience} about {title}."
        try:
            blog_content = llm.invoke(prompt)
        except Exception as e:
            return Response({"error": f"Model error: {str(e)}"}, status=500)

        return Response({"blog_content": blog_content}, status=200)

# ----------------- Save Blog -----------------
class SaveBlogAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        title = request.data.get("title")
        content = request.data.get("content")

        if not title or not content:
            return Response({"error": "Title and content are required"}, status=400)

        blog = Blog.objects.create(title=title, content=content, author=request.user)
        return Response(BlogSerializer(blog).data, status=201)

# ----------------- Blog History -----------------
class BlogHistoryAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        blogs = Blog.objects.filter(author=request.user)
        return Response(BlogSerializer(blogs, many=True).data, status=200)
