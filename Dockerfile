FROM python:3.10-slim

WORKDIR /app

# Установка системных зависимостей
RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    gettext \
    nodejs \
    npm \
    && rm -rf /var/lib/apt/lists/*

# Python зависимости
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Node.js зависимости для Tailwind
COPY theme/package.json theme/package-lock.json ./theme/
RUN cd theme && npm ci --only=production

# Проект
COPY . .

# Сборка Tailwind CSS
RUN cd theme && npm run build

# Готово! Статика будет собрана при запуске (в команде)
# (убрали из Dockerfile, чтобы не зависеть от БД на этапе сборки)

CMD ["sh", "-c", "python manage.py collectstatic --noinput && python manage.py migrate --noinput && gunicorn config.wsgi:application --bind 0.0.0.0:8000 --workers 3"]