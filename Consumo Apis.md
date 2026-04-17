# Consumo de APIs

## Base URL

- Local: `http://127.0.0.1:8000/api`

## Autenticacion JWT

- Header para endpoints protegidos:

```http
Authorization: Bearer <access_token>
Content-Type: application/json
```

## Formato estandar de respuesta

```json
{
  "message": "Texto de estado",
  "data": {},
  "pagination": null,
  "error": null
}
```

## Paginacion y filtros comunes en GET de listado

- Query params disponibles:
  - `page` (default `1`)
  - `page_size` (`10`, `20`, `50`)
  - `search` (texto libre)
  - `order` (`asc` o `desc`)

---

## Carpeta Users

### POST `/login/` (publica)

Request:

```json
{
  "email": "admin@demo.com",
  "password": "12345678"
}
```

Response 200:

```json
{
  "message": "Inicio de sesion correcto",
  "data": {
    "user_id": 1,
    "access": "jwt_access_token",
    "refresh": "jwt_refresh_token",
    "session_started_at": "2026-04-17T14:30:00Z"
  },
  "pagination": null,
  "error": null
}
```

### POST `/register/` (publica)

Request:

```json
{
  "email": "admin@demo.com",
  "password": "12345678",
  "username": "admin"
}
```

Response 201:

```json
{
  "message": "Usuario registrado",
  "data": {
    "id": 1,
    "email": "admin@demo.com",
    "username": "admin",
    "is_staff": true,
    "is_superuser": true
  },
  "pagination": null,
  "error": null
}
```

### POST `/logout/` (publica por diseno actual, usa refresh)

Request:

```json
{
  "refresh": "jwt_refresh_token"
}
```

Response 200:

```json
{
  "message": "Sesion cerrada",
  "data": {
    "user_id": 1,
    "session_started_at": "2026-04-17T14:30:00Z",
    "session_ended_at": "2026-04-17T14:45:00Z"
  },
  "pagination": null,
  "error": null
}
```

---

## Carpeta Document Types (protegidas con JWT)

### GET `/document-types/`

- Devuelve solo activos (`is_active=true`).
- Soporta `page`, `page_size`, `search`, `order`.

Ejemplo:
`/document-types/?page=1&page_size=10&search=doc&order=desc`

Response 200:

```json
{
  "message": "Registros activos obtenidos",
  "data": {
    "items": [
      {
        "id": 1,
        "name": "DNI",
        "description": "Documento nacional",
        "is_active": true,
        "deleted_at": null,
        "created_at": "2026-04-17T14:30:00Z",
        "updated_at": "2026-04-17T14:30:00Z"
      }
    ]
  },
  "pagination": {
    "page": 1,
    "page_size": 10,
    "total_items": 1,
    "total_pages": 1,
    "has_next": false,
    "has_previous": false
  },
  "error": null
}
```

### GET `/document-types/inactive/`

- Devuelve solo inactivos (`is_active=false`).
- Soporta `page`, `page_size`, `search`, `order`.

Response 200: mismo formato paginado.

### GET `/document-types/{id}/`

Response 200:

```json
{
  "message": "Registro obtenido",
  "data": {
    "id": 1,
    "name": "DNI",
    "description": "Documento nacional",
    "is_active": true,
    "deleted_at": null,
    "created_at": "2026-04-17T14:30:00Z",
    "updated_at": "2026-04-17T14:30:00Z"
  },
  "pagination": null,
  "error": null
}
```

### POST `/document-types/`

Request:

```json
{
  "name": "Pasaporte",
  "description": "Documento internacional",
  "is_active": true
}
```

Response 201:

```json
{
  "message": "Registro creado",
  "data": {
    "id": 2,
    "name": "Pasaporte",
    "description": "Documento internacional",
    "is_active": true,
    "deleted_at": null,
    "created_at": "2026-04-17T14:35:00Z",
    "updated_at": "2026-04-17T14:35:00Z"
  },
  "pagination": null,
  "error": null
}
```

### PUT `/document-types/{id}/`

Request:

```json
{
  "name": "Pasaporte",
  "description": "Documento internacional actualizado",
  "is_active": true
}
```

Response 200:

```json
{
  "message": "Registro actualizado",
  "data": {
    "id": 2,
    "name": "Pasaporte",
    "description": "Documento internacional actualizado",
    "is_active": true,
    "deleted_at": null,
    "created_at": "2026-04-17T14:35:00Z",
    "updated_at": "2026-04-17T14:40:00Z"
  },
  "pagination": null,
  "error": null
}
```

### DELETE `/document-types/{id}/`

- Soft delete: marca `is_active=false` y setea `deleted_at`.

Response 200:

```json
{
  "message": "Registro eliminado",
  "data": {
    "id": 2,
    "name": "Pasaporte",
    "is_active": false,
    "deleted_at": "2026-04-17T14:45:00Z"
  },
  "pagination": null,
  "error": null
}
```

---

## Carpeta Audit (protegidas con JWT)

### GET `/audits/`

- Soporta `page`, `page_size`, `search`, `order`.
- Filtros extra:
  - `action=LOGIN|LOGOUT|REGISTER|CREATE|UPDATE|DELETE`
  - `session_state=ACTIVE|INACTIVE`

Ejemplo:
`/audits/?page=1&page_size=20&action=CREATE&order=desc`

Response 200:

```json
{
  "message": "Auditoria obtenida",
  "data": {
    "items": [
      {
        "id": 10,
        "user_id": 1,
        "user_email": "admin@demo.com",
        "action": "CREATE",
        "message": "Creo registro en tipo de documento",
        "entity_type": "DocumentType",
        "entity_id": 2,
        "entity_name": "Pasaporte",
        "session_state": "",
        "session_started_at": null,
        "session_ended_at": null,
        "ip_address": "127.0.0.1",
        "created_at": "2026-04-17T14:35:00Z"
      }
    ]
  },
  "pagination": {
    "page": 1,
    "page_size": 20,
    "total_items": 1,
    "total_pages": 1,
    "has_next": false,
    "has_previous": false
  },
  "error": null
}
```

---

## Errores comunes

### 400 Datos invalidos

```json
{
  "message": "Invalid data",
  "data": {},
  "pagination": null,
  "error": {
    "campo": ["detalle de validacion"]
  }
}
```

### 401 Credenciales invalidas

```json
{
  "message": "Invalid credentials",
  "data": {},
  "pagination": null,
  "error": "Invalid credentials"
}
```

### 404 No encontrado

```json
{
  "message": "Document type not found",
  "data": {},
  "pagination": null,
  "error": "Document type not found"
}
```

### 500 Error interno

```json
{
  "message": "Internal server error",
  "data": {},
  "pagination": null,
  "error": "detalle tecnico"
}
```
