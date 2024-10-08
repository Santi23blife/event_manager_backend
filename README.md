# Event Manager Backend API

Este proyecto es un backend desarrollado en Django y Django REST Framework para manejar una aplicación de gestión de eventos. El usuario puede registrarse, iniciar sesión y realizar operaciones CRUD sobre eventos.

## Requisitos

- Python 3.10+
- Django 4.x
- Django REST Framework
- Simple JWT para autenticación con JWT

## Instalación

1. Clona el repositorio.

   ```bash
   git clone https://github.com/tu-usuario/event-manager-backend.git
   cd event-manager-backend
   ```

2. Crea y activa un entorno virtual.

   ```bash
   python -m venv env
   source env/bin/activate  # Linux/Mac
   env\Scripts\activate  # Windows
   ```

3. Instala las dependencias.

   ```bash
   pip install -r requirements.txt
   ```

4. Aplica las migraciones.

   ```bash
   py manage.py migrate
   ```

5. Crea un superusuario para acceder al panel de administración.

   ```bash
   py manage.py createsuperuser
   ```

6. Inicia el servidor de desarrollo.
   ```bash
   py manage.py runserver
   ```

## Endpoints Principales

### **Ruta raíz**

```http
GET /api/
```

Devuelve un mensaje "Hola Mundo".

#### Respuesta de ejemplo:

```json
{
  "message": "Hola Mundo"
}
```

### **Autenticación JWT**

#### Obtener Token JWT

```http
POST /api/token/
```

Este endpoint devuelve un token de acceso y un token de actualización para la autenticación del usuario.

- **Body**:
  ```json
  {
    "username": "usuario",
    "password": "contraseña"
  }
  ```

#### Renovar Token JWT

```http
POST /api/token/refresh/
```

Renueva el token de acceso usando el token de actualización.

- **Body**:
  ```json
  {
    "refresh": "token_de_actualización"
  }
  ```

### **Registro de Usuarios**

#### Crear Usuario

```http
POST /api/auth/register/
```

Este endpoint permite registrar un nuevo usuario.

- **Body**:
  ```json
  {
    "username": "nuevo_usuario",
    "email": "email@ejemplo.com",
    "first_name": "Nombre",
    "last_name": "Apellido",
    "password": "contraseña",
    "password2": "contraseña"
  }
  ```

#### Respuesta de ejemplo:

```json
{
  "id": 1,
  "username": "nuevo_usuario",
  "email": "email@ejemplo.com",
  "first_name": "Nombre",
  "last_name": "Apellido"
}
```

### **CRUD de Eventos**

#### Listar Eventos

```http
GET /api/events/
```

Devuelve la lista de eventos creados por el usuario autenticado.

#### Crear Evento

```http
POST /api/events/
```

Permite al usuario autenticado crear un nuevo evento.

- **Body**:
  ```json
  {
    "name": "Concierto de rock",
    "description": "Un concierto increíble",
    "place": "Estadio Nacional",
    "date": "2024-09-30T20:00:00",
    "activated_notification": true
  }
  ```

#### Respuesta de ejemplo:

```json
{
  "id": 1,
  "name": "Concierto de rock",
  "description": "Un concierto increíble",
  "place": "Estadio Nacional",
  "date": "2024-09-30T20:00:00",
  "date_creation": "2024-09-25T10:30:00",
  "user": 1,
  "activated_notification": true
}
```

#### Detalles de un Evento

```http
GET /api/events/{id}/
```

Devuelve los detalles de un evento específico por su `id`.

#### Actualizar Evento

```http
PUT /api/events/{id}/
```

Permite al usuario actualizar un evento existente.

- **Body** (ejemplo):
  ```json
  {
    "name": "Concierto de jazz",
    "description": "Concierto al aire libre",
    "place": "Parque Central",
    "date": "2024-10-05T18:00:00",
    "activated_notification": false
  }
  ```

#### Eliminar Evento

```http
DELETE /api/events/{id}/
```

Permite al usuario eliminar un evento.

## Modelos

### **Modelo de Usuario**

El modelo de usuario proviene de `django.contrib.auth.models.User`.

### **Modelo de Evento**

El modelo de eventos tiene los siguientes campos:

- **name**: Nombre del evento (máx. 200 caracteres).
- **description**: Descripción del evento.
- **place**: Lugar del evento.
- **date**: Fecha y hora del evento.
- **date_creation**: Fecha de creación (se establece automáticamente).
- **user**: Usuario que creó el evento (llave foránea).
- **activated_notification**: Booleano que indica si la notificación está activada o no.

## Rutas

- `GET /api/`: Ruta raíz que devuelve "Hola Mundo".
- `POST /api/auth/register/`: Registrar un nuevo usuario.
- `POST /api/token/`: Obtener token JWT.
- `POST /api/token/refresh/`: Renovar token JWT.
- `GET /api/events/`: Listar eventos.
- `POST /api/events/`: Crear evento.
- `GET /api/events/{id}/`: Obtener detalles de un evento.
- `PUT /api/events/{id}/`: Actualizar evento.
- `DELETE /api/events/{id}/`: Eliminar evento.

## Autenticación

Este proyecto usa JWT (JSON Web Token) para la autenticación de usuarios. Asegúrate de obtener el token de acceso (`access_token`) y usarlo en el encabezado `Authorization: Bearer {token}` para hacer peticiones a los endpoints protegidos.

## Contribuir

Si deseas contribuir a este proyecto, sigue estos pasos:

1. Haz un fork del repositorio.
2. Crea una nueva rama con tu función/corrección: `git checkout -b mi-funcion`.
3. Realiza tus cambios y guarda los commits de acuerdo a [Conventional Commits](https://www.conventionalcommits.org).
4. Envía tu rama con un PR.
