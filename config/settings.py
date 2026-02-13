"""
Django settings for config project.
Production-ready with environment variables and security defaults.
"""

import os
from pathlib import Path


try:
    import dj_database_url
except ImportError:
    dj_database_url = None

from dotenv import load_dotenv

# === ИСПРАВЛЕНО: Сначала загружаем .env, ПОТОМ читаем переменные ===
BASE_DIR = Path(__file__).resolve().parent.parent

# Загружаем .env сразу
load_dotenv(BASE_DIR / ".env")  # ← Грузим всегда (в dev и тестах). В prod — можно не использовать.

def env_bool(name: str, default: bool = False) -> bool:
    raw = os.getenv(name)
    if raw is None:
        return default
    return raw.strip().lower() in {"1", "true", "yes", "y", "on"}


def env_list(name: str, default: list[str] | None = None) -> list[str]:
    raw = os.getenv(name)
    if raw is None:
        return default or []
    return [x.strip() for x in raw.split(",") if x.strip()]


# Теперь можно безопасно читать SECRET_KEY
SECRET_KEY = os.getenv("SECRET_KEY")

if not SECRET_KEY:
    if not os.getenv("DJANGO_DEBUG", "0").lower() in ("1", "true", "yes"):
        raise ValueError("SECRET_KEY обязательна в продакшене!")
    else:
        # Только для разработки
        SECRET_KEY = "django-insecure-please-change-in-production"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env_bool("DJANGO_DEBUG", default=False)

# Hosts / CSRF
ALLOWED_HOSTS = env_list(
    "DJANGO_ALLOWED_HOSTS",
)

# CSRF trusted origins (для HTTPS)
CSRF_TRUSTED_ORIGINS = env_list(
    "CSRF_TRUSTED_ORIGINS",
)

# Разрешить * только если DEBUG=True
if DEBUG:
    ALLOWED_HOSTS = ["*"]
    CSRF_TRUSTED_ORIGINS += ["http://localhost:8000", "http://127.0.0.1:8000"]