# Встановлюємо базовий образ з Python
FROM python:3.10-slim

# Встановлюємо залежності для PostgreSQL та інші утиліти
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Створюємо та переходимо у робочу директорію
WORKDIR /app

# Копіюємо файл requirements.txt
COPY requirements.txt /app/

# Копіюємо проект
COPY . /app/

# Встановлюємо python-dotenv
RUN pip install python-dotenv

# Встановлюємо залежності з requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Виставляємо перемінну оточення для Django
ENV DJANGO_SETTINGS_MODULE=config.settings

# Виконуємо команди для запуску проекту
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "config.wsgi:application"]
