# Usamos una imagen liviana de Python
FROM python:3.11-alpine

# Definir variable de entorno para logs sin buffering
ENV PYTHONUNBUFFERED=1

# Instalar dependencias del sistema necesarias para compilar psycopg2 y otras librerías
RUN apk add --no-cache \
    gcc \
    musl-dev \
    postgresql-dev \
    postgresql-client \
    libffi-dev \
    python3-dev \
    jpeg-dev \
    zlib-dev \
    build-base && \
    pip install --no-cache-dir --upgrade pip

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar solo el archivo de dependencias primero para aprovechar la caché de Docker
COPY requirements.txt .

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código fuente de la app
COPY . .

# Copiar el script de entrada
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Comando por defecto al ejecutar el contenedor
ENTRYPOINT ["/entrypoint.sh"]
