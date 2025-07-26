import os
from pathlib import Path
from datetime import timedelta
import environ

# --------------------------
# Load environment variables
# --------------------------
BASE_DIR = Path(__file__).resolve().parent.parent
env = environ.Env(DEBUG=(bool, False))
environ.Env.read_env(os.path.join(BASE_DIR, ".env"))

# --------------------------
# Security settings
# --------------------------
SECRET_KEY = env("SECRET_KEY", default="your-default-secret-key")
DEBUG = env("DEBUG", default=True)
ALLOWED_HOSTS = ["127.0.0.1", "localhost"]

# --------------------------
# Installed applications
# --------------------------
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "api",  # Your API app
    "rest_framework",
    "rest_framework_simplejwt",
    "corsheaders",  # Enable CORS for Streamlit
]

# --------------------------
# DRF Authentication (JWT-based)
# --------------------------
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.AllowAny",  # Allow registration & login without auth
    ],
}

# --------------------------
# JWT Token Configuration
# --------------------------
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(days=1),  # Users stay logged in for 1 day
    "REFRESH_TOKEN_LIFETIME": timedelta(days=7),
    "ROTATE_REFRESH_TOKENS": True,
    "BLACKLIST_AFTER_ROTATION": True,
    "AUTH_HEADER_TYPES": ("Bearer",),
}

# --------------------------
# Middleware
# --------------------------
MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# --------------------------
# CORS Settings
# --------------------------
CORS_ALLOWED_ORIGINS = [
    "http://localhost:8501",  # Streamlit frontend
    "http://127.0.0.1:8501",
]
CORS_ALLOW_CREDENTIALS = True

# --------------------------
# Database Configuration (MySQL)
# --------------------------
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": env("MYSQL_DB_NAME", default="blog_db"),
        "USER": env("MYSQL_USER", default="root"),
        "PASSWORD": env("MYSQL_PASSWORD", default="root"),
        "HOST": env("MYSQL_HOST", default="localhost"),
        "PORT": env("MYSQL_PORT", default="3306"),
        "OPTIONS": {"charset": "utf8mb4"},
    }
}

# --------------------------
# Static & Media Files
# --------------------------
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# --------------------------
# Custom User Model
# --------------------------
AUTH_USER_MODEL = "api.User"

# --------------------------
# Templates
# --------------------------
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# --------------------------
# URL & WSGI/ASGI
# --------------------------
ROOT_URLCONF = "BlogGen.urls"
WSGI_APPLICATION = "BlogGen.wsgi.application"
ASGI_APPLICATION = "BlogGen.asgi.application"

# --------------------------
# Internationalization
# --------------------------
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# --------------------------
# Default primary key field type
# --------------------------
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
