from django.urls import path
from api.views import RegisterAPIView, LoginAPIView, BlogGenerateAPIView, SaveBlogAPIView, BlogHistoryAPIView, home

urlpatterns = [
    path("", home, name="home"),
    path("register/", RegisterAPIView.as_view(), name="register"),
    path("login/", LoginAPIView.as_view(), name="login"),
    path("generate-blog/", BlogGenerateAPIView.as_view(), name="generate-blog"),
    path("save-blog/", SaveBlogAPIView.as_view(), name="save-blog"),  # ✅ FIXED: Added missing endpoint
    path("blogs/", BlogHistoryAPIView.as_view(), name="blogs"),
]
