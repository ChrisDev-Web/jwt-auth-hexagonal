# Eventos y modelo de auditoría

## Tabla `audit_events`

Definida en `infrastructure/db/models.py` (`AuditEventModel`).

Campos relevantes:

| Campo | Uso |
|-------|-----|
| `user` | Usuario que originó el evento (puede ser null en casos edge). |
| `action` | `LOGIN`, `LOGOUT`, `REGISTER`, `CREATE`, `UPDATE`, `DELETE`. |
| `message` | Texto para el frontend (ej. “Creo registro en tipo de documento”). |
| `entity_type` | Ej. `DocumentType`, `User`. |
| `entity_id` / `entity_name` | Identificación legible del recurso. |
| `session_state` | `ACTIVE` / `INACTIVE` en flujos de sesión. |
| `session_started_at` / `session_ended_at` | Ventana temporal de sesión cuando aplica. |
| `ip_address` | IP del cliente (primera de `X-Forwarded-For`, o `X-Real-IP`, o `REMOTE_ADDR`). |
| `created_at` | Momento del registro del evento. |

## Comportamiento de login / logout

- **Login**: se crea un evento `LOGIN` con `session_state=ACTIVE` y `session_started_at`.
- **Logout**: se intenta **actualizar** el último `LOGIN` activo del usuario a `INACTIVE` y `session_ended_at`. Si no hay match, se crea un evento `LOGOUT`.

## Acciones sobre datos

Para `document_types`, el mensaje mostrado al usuario no expone la URL interna; solo describe la acción en lenguaje de negocio.
