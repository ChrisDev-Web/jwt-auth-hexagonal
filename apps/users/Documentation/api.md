# API del módulo `users`

**Base URL** (desarrollo): `http://127.0.0.1:8000/api`

Todas las rutas bajo `users` son **públicas** (`AllowAny`) para permitir el flujo del frontend antes de obtener JWT.

| Método | Ruta | Descripción |
|--------|------|-------------|
| `POST` | `/login/` | Credenciales → `access`, `refresh`, `user_id`, `session_started_at`. |
| `POST` | `/register/` | Alta de usuario → datos del usuario creado. |
| `POST` | `/logout/` | Cuerpo con `refresh` → cierra sesión y revoca tokens en BD. |

## Cabeceras

- `Content-Type: application/json`
- En login/register/logout **no** se envía `Authorization` (salvo que decidas extender el diseño).

## Más detalle

Ejemplos de cuerpos y respuestas: raíz del proyecto → `Consumo Apis.md` (sección Users).
