from django.http import JsonResponse

def home(request):
    return JsonResponse({"message": "Welcome to the Blog Generator API!"})
def register_user(request):
    return JsonResponse({"message": "Register API working!"})

def login_user(request):
    return JsonResponse({"message": "Login API working!"})

def blog_view(request):
    return JsonResponse({"message": "Blog API working!"})
