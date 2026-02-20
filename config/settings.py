import os
from pathlib import Path
from decouple import config

# Основные пути
BASE_DIR = Path(__file__).resolve().parent.parent

# ============================================================================
# БЕЗОПАСНОСТЬ — переменные окружения
# ============================================================================
DEBUG = config('DEBUG', default=False, cast=bool)

SECRET_KEY = config('SECRET_KEY')

ALLOWED_HOSTS = ['*'] 
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
USE_X_FORWARDED_HOST = True


# ============================================================================
# ПРИЛОЖЕНИЯ
# ============================================================================
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "polls.apps.PollsConfig",  # ваше приложение
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
#    "whitenoise.middleware.WhiteNoiseMiddleware",  # ← для раздачи статики
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"

# ============================================================================
# БАЗА ДАННЫХ — PostgreSQL для продакшена
# ============================================================================


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": config('DB_NAME', 'polling_db'),
        "USER": config('DB_USER', 'polling_user'),
        "PASSWORD": config('DB_PASSWORD', ''),
        "HOST": config('DB_HOST', 'localhost'),
        "PORT": config('DB_PORT', '5432'),
    }
}

# ==

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# ============================================================================
# ЛОКАЛИЗАЦИЯ
# ============================================================================
LANGUAGE_CODE = "ru-ru"
TIME_ZONE = "Asia/Krasnoyarsk"
USE_I18N = True
USE_TZ = True

# ============================================================================
# СТАТИЧЕСКИЕ ФАЙЛЫ
# ============================================================================
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_DIRS = [
    BASE_DIR / "frontend" / "static",
]

# WhiteNoise для сжатия и кэширования статики
#STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# ============================================================================
# АВТО-КЛЮЧ
# ============================================================================

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# ============================================================================
# РЕДИРЕКТЫ ПОСЛЕ АВТОРИЗАЦИИ
# ============================================================================
LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/"
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
