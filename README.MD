# 🚀 Backend Django Avanzado con Docker, JWT y UUID

Este proyecto es una base completa y lista para usar de un backend Django dockerizado. Diseñado para servir como punto de partida sólido para cualquier desarrollador que necesite un backend robusto con características modernas. Incluye PostgreSQL como base de datos, autenticación JWT con gestión avanzada de usuarios mediante UUID, documentación de API integrada, y está optimizado para desarrollo y producción.

---

## 📂 Estructura del Proyecto

```
📦 django-jwt
├── 📂 backend_django         # Proyecto Django principal
│   ├── 📜 Dockerfile         # Configuración de la imagen Docker
│   ├── 📜 manage.py          # CLI de Django
│   ├── 📂 backend_django     # Configuración principal del proyecto
│   │   ├── 📜 settings.py    # Configuración con variables de entorno
│   │   ├── 📜 urls.py        # Endpoints y documentación API
│   ├── 📂 authentication     # Sistema avanzado de autenticación
│   │   ├── 📜 models.py      # Modelos con UUID y perfiles
│   │   ├── 📜 views.py       # ViewSets para API RESTful
│   │   ├── 📜 serializers.py # Serialización para API
│   ├── 📂 media              # Almacenamiento de archivos de usuario
│   ├── 📂 static             # Archivos estáticos
│   ├── 📂 staticfiles        # Archivos estáticos compilados
│   ├── 📜 requirements.txt   # Dependencias organizadas por categorías
│   ├── 📜 entrypoint.sh      # Automatización de inicialización
├── 📜 docker-compose.yml     # Orquestación de servicios
├── 📜 .env                   # Variables de entorno (no incluir en VCS)
```

---

## 🛠️ Configuración del Entorno

### 📌 1. Crear el archivo `.env`
Antes de ejecutar el proyecto, crea un archivo `.env` en la raíz con el siguiente contenido:

```ini
# Configuración de Django
SECRET_KEY=tu-clave-secreta-compleja-y-unica
DEBUG=True
ALLOWED_HOSTS=*

# Configuración de PostgreSQL
POSTGRES_DB=tu_base_datos
POSTGRES_USER=tu_usuario
POSTGRES_PASSWORD=tu_contraseña_segura
POSTGRES_HOST=db_postgres
POSTGRES_PORT=5432
```

> 🔒 **Importante:** El archivo `.env` ya está excluido en `.gitignore` para proteger tus credenciales.

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

## 🔑 API RESTful y Endpoints

### Autenticación y Gestión de Usuarios

- **Registro**: `POST /api/user/register/`
- **Obtener token JWT**: `POST /api/token/`
- **Refrescar token**: `POST /api/token/refresh/`
- **Gestión de usuarios completa**:
  - Listar usuarios: `GET /api/users/`
  - Obtener usuario por ID: `GET /api/users/{id}/`
  - Obtener usuario por UUID: `GET /api/users/{uuid}/`
  - Detalles del usuario actual: `GET /api/users/me/`
  - Actualizar perfil propio: `PATCH /api/users/update_me/`

### Perfiles de Usuario

- **Listar perfiles**: `GET /api/profiles/`
- **Obtener perfil por UUID**: `GET /api/profiles/{uuid}/`

### Uso de JWT en Peticiones

```
Authorization: Bearer <tu-token-jwt>
```

### Documentación Interactiva

- **Documentación completa**: `/api/docs/`

---

## 📌 Acceso a la Aplicación

- **Panel de Administración**: http://localhost:8000/admin/
- **API RESTful**: http://localhost:8000/api/
- **Documentación API**: http://localhost:8000/api/docs/
- **Base de datos PostgreSQL**: `localhost:5433` (usar credenciales del `.env`)

> ℹ️ Si implementas un frontend, puedes conectarlo fácilmente a estos endpoints.

---

## 🧩 Características Principales

- **Django 5.1+**: Framework web de Python moderno y mantenido
- **PostgreSQL**: Base de datos relacional de alto rendimiento
- **Sistema de Usuarios Avanzado**:
  - Identificación mediante UUID (no secuencial ni predecible)
  - Perfiles de usuario extensibles con avatares
  - Endpoints completos para frontend (CRUD)
- **Autenticación JWT**: Tokens seguros con refresh automático
- **Documentación API Integrada**: Endpoints autodocumentados
- **Docker y Docker Compose**: Entorno consistente y reproducible
- **Optimizado para Producción**:
  - Gunicorn como servidor WSGI de alto rendimiento
  - WhiteNoise para servir archivos estáticos eficientemente
  - Variables de entorno para configuración segura
- **REST API Completa**: Endpoints listos para consumir desde cualquier frontend

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

## 💡 Plantilla para Tu Próximo Proyecto

Este proyecto está diseñado como base sólida para cualquier aplicación que requiera un backend robusto. Está pensado para ser:

- **Extensible**: Añade nuevas apps y funcionalidades fácilmente
- **Seguro**: Implementa buenas prácticas de seguridad desde el inicio
- **Escalable**: Diseñado para crecer con tu aplicación
- **Moderno**: Utiliza UUID para mayor seguridad en las IDs
- **Listo para frontend**: API completa documentada

## 📚 Recursos y Documentación

- [Django](https://docs.djangoproject.com/) - Framework web
- [Django REST Framework](https://www.django-rest-framework.org/) - API RESTful
- [Simple JWT](https://django-rest-framework-simplejwt.readthedocs.io/) - Autenticación
- [Docker](https://docs.docker.com/) - Contenedorización
- [PostgreSQL](https://www.postgresql.org/docs/) - Base de datos

