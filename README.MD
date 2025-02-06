# 📌 Proyecto Django con Docker y PostgreSQL

Este proyecto es una aplicación Django configurada para ejecutarse dentro de contenedores Docker. Utiliza PostgreSQL como base de datos y está estructurado para un despliegue eficiente y modular.

---

## 📂 Estructura del Proyecto

```
📦 proyecto
├── 📂 backend_django       # Carpeta del proyecto Django
│   ├── 📜 Dockerfile       # Dockerfile para construir la imagen del backend
│   ├── 📜 manage.py        # Archivo de gestión de Django
│   ├── 📂 backend_django   # Código fuente del proyecto Django
│   ├── 📜 requirements.txt # Dependencias del proyecto
│   ├── 📂 ...              # Otras carpetas y archivos de Django
├── 📜 docker-compose.yml   # Archivo para gestionar los servicios con Docker Compose
├── 📜 .env                 # Archivo con variables de entorno (no incluir en repositorio)
├── 📜 .dockerignore        # Archivos y carpetas a ignorar en la imagen de Docker
```

---

## 🛠️ Configuración del Entorno

### 📌 1. Crear el archivo `.env`
Antes de ejecutar el proyecto, se debe crear un archivo `.env` en la raíz del proyecto con el siguiente formato:

```ini
# Configuración de Django
DJANGO_SECRET_KEY=django-insecure-reemplazar-por-una-clave-segura
DEBUG=True
ALLOWED_HOSTS=*

# Configuración de PostgreSQL
POSTGRES_DB=mi_base_datos
POSTGRES_USER=mi_usuario
POSTGRES_PASSWORD=mi_contraseña_segura
POSTGRES_HOST=db_postgres
POSTGRES_PORT=5432
```

> ⚠️ **Nota:** No compartas este archivo públicamente, ya que contiene información sensible.

---

## 🚀 Levantar el Proyecto

1. **Construir los contenedores**
   ```sh
   docker-compose build
   ```
2. **Iniciar los servicios**
   ```sh
   docker-compose up -d
   ```
3. **Verificar los contenedores en ejecución**
   ```sh
   docker ps
   ```
4. **Acceder a los logs** (opcional)
   ```sh
   docker-compose logs -f backend_django
   ```
5. **Detener los contenedores**
   ```sh
   docker-compose down
   ```

---

## 📌 Acceso a la Aplicación

- **Backend Django**: http://localhost:8000
- **Base de datos PostgreSQL**: Disponible en `localhost:5433`

Si deseas acceder a la base de datos desde un cliente externo, usa las credenciales definidas en el archivo `.env`.

---

## 🛑 Notas Importantes

- Asegúrate de tener **Docker** y **Docker Compose** instalados en tu sistema.
- El archivo `.dockerignore` debe contener archivos innecesarios para la imagen de Docker, por ejemplo:
  ```
  __pycache__/
  .git/
  .venv/
  db.sqlite3
  *.pyc
  ```
- Para producción, se recomienda definir variables de entorno de forma segura en lugar de usar `.env` directamente.

---

## 📚 Recursos Adicionales
- [Documentación oficial de Django](https://docs.djangoproject.com/)
- [Guía de Docker](https://docs.docker.com/)
- [Guía de PostgreSQL](https://www.postgresql.org/docs/)

