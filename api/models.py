from django.db import models
from django.contrib.auth.models import AbstractUser

# ✅ Custom User Model
class User(AbstractUser):
    email = models.EmailField(unique=True)

# ✅ Blog Model (Now Correctly Uses `author` ForeignKey)
class Blog(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blogs")  # ✅ Fix: Use "author" instead of "user"
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
