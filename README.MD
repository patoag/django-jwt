# 📌 Proyecto Django con Docker, PostgreSQL y JWT Authentication

Este proyecto es una plantilla de aplicación Django configurada para ejecutarse dentro de contenedores Docker. Utiliza PostgreSQL como base de datos, autenticación JWT para APIs seguras, y está estructurado para un despliegue eficiente y modular.

---

## 📂 Estructura del Proyecto

```
📦 proyecto
├── 📂 backend_django         # Carpeta del proyecto Django
│   ├── 📜 Dockerfile         # Dockerfile para construir la imagen del backend
│   ├── 📜 manage.py          # Archivo de gestión de Django
│   ├── 📂 backend_django     # Configuración del proyecto Django
│   ├── 📂 authentication     # App de autenticación con JWT
│   ├── 📜 requirements.txt   # Dependencias del proyecto
│   ├── 📜 entrypoint.sh      # Script de inicialización para Docker
│   ├── 📂 staticfiles        # Archivos estáticos compilados
│   ├── 📂 static             # Archivos estáticos del proyecto
├── 📜 docker-compose.yml     # Configuración de servicios con Docker Compose
├── 📜 .env                   # Variables de entorno (no incluir en repositorio)
├── 📜 .dockerignore          # Archivos y carpetas a ignorar en Docker
```

---

## 🛠️ Configuración del Entorno

### 📌 1. Crear el archivo `.env`
Antes de ejecutar el proyecto, crea un archivo `.env` en la raíz del proyecto con el siguiente formato:

```ini
# Configuración de Django
DJANGO_SECRET_KEY=django-insecure-clave-segura-personalizada
DEBUG=True
ALLOWED_HOSTS=*

# Configuración de PostgreSQL
POSTGRES_DB=tu_base_datos
POSTGRES_USER=tu_usuario
POSTGRES_PASSWORD=tu_contraseña_segura
POSTGRES_HOST=db_postgres
POSTGRES_PORT=5432
```

> ⚠️ **Nota:** No compartas este archivo públicamente, ya que contiene información sensible. Asegúrate de añadir `.env` a tu archivo `.gitignore`.

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
   El flag `-d` ejecuta los contenedores en modo detached (segundo plano).

3. **Verificar los contenedores en ejecución**
   ```sh
   docker ps
   ```

4. **Acceder a los logs** (opcional)
   ```sh
   # Ver logs de un servicio específico
   docker-compose logs -f backend_django
   
   # Ver logs de todos los servicios
   docker-compose logs -f
   ```

5. **Detener los contenedores**
   ```sh
   docker-compose down
   ```

---

## 👤 Gestión de Usuarios Administradores

### Crear un Superusuario

Para crear un superusuario y acceder al panel de administración de Django, ejecuta:

```sh
# Formato general
docker-compose exec [nombre-del-servicio] python manage.py createsuperuser

# Para este proyecto
docker-compose exec backend_django python manage.py createsuperuser
```

Sigue las instrucciones interactivas para ingresar nombre de usuario, email y contraseña.

### Crear un Superusuario con Datos Predefinidos

Para crear un superusuario sin interacción (útil para scripts):

```sh
# Crear superusuario con credenciales predefinidas
docker-compose exec backend_django python manage.py createsuperuser --username admin --email admin@example.com --noinput

# Establecer contraseña para el usuario creado
docker-compose exec backend_django python manage.py shell -c "from django.contrib.auth.models import User; user = User.objects.get(username='admin'); user.set_password('contraseña_segura'); user.save(); print('Contraseña actualizada con éxito')"
```

---

## 🔑 Endpoints de Autenticación JWT

Este proyecto incluye autenticación JWT lista para usar:

- **Registro de usuario**: `/api/user/register/`
- **Obtener token**: `/api/token/`
- **Refrescar token**: `/api/token/refresh/`

Para usar la autenticación en tus solicitudes HTTP, incluye el token en el encabezado:

```
Authorization: Bearer <tu-token-jwt>
```

---

## 📌 Acceso a la Aplicación

- **Panel de Administración**: http://localhost:8000/admin/
- **API Django Rest Framework**: http://localhost:8000/api/
- **Base de datos PostgreSQL**: Disponible en `localhost:5433`

Si deseas acceder a la base de datos desde un cliente externo, usa las credenciales definidas en el archivo `.env`.

---

## 🧩 Características Principales

- **Django 5.1+**: Framework web de Python de alto nivel
- **PostgreSQL**: Base de datos relacional robusta
- **JWT Authentication**: Autenticación segura para APIs
- **Docker & Docker Compose**: Contenerización y orquestación
- **WhiteNoise**: Servicio optimizado de archivos estáticos
- **Gunicorn**: Servidor WSGI para entornos de producción
- **Django REST Framework**: Construcción de APIs RESTful

---

## 🛠️ Comandos Útiles de Docker

```sh
# Ejecutar migraciones manualmente
docker-compose exec backend_django python manage.py migrate

# Crear una nueva app Django
docker-compose exec backend_django python manage.py startapp nombre_app

# Recopilar archivos estáticos
docker-compose exec backend_django python manage.py collectstatic --noinput

# Abrir shell de Django
docker-compose exec backend_django python manage.py shell

# Acceder a la shell de postgres
docker-compose exec db_postgres psql -U $POSTGRES_USER -d $POSTGRES_DB
```

---

## 🛑 Notas Importantes

- Asegúrate de tener **Docker** y **Docker Compose** instalados en tu sistema.
- El archivo `.dockerignore` debe contener archivos innecesarios para la imagen de Docker.
- Los archivos estáticos se gestionan con WhiteNoise para entornos de producción.
- Para producción, se recomienda definir variables de entorno de forma segura en lugar de usar `.env` directamente.
- El archivo `entrypoint.sh` ejecuta automáticamente migraciones y recopila archivos estáticos al iniciar el contenedor.

---

## 📚 Recursos Adicionales
- [Documentación oficial de Django](https://docs.djangoproject.com/)
- [Documentación de Django REST Framework](https://www.django-rest-framework.org/)
- [Documentación de Simple JWT](https://django-rest-framework-simplejwt.readthedocs.io/)
- [Guía de Docker](https://docs.docker.com/)
- [Guía de PostgreSQL](https://www.postgresql.org/docs/)

