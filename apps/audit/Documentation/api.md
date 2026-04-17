# API del módulo `audit`

**Base URL**: `http://127.0.0.1:8000/api`

**Autenticación**: `Authorization: Bearer <access_token>`

## Endpoint

| Método | Ruta | Descripción |
|--------|------|-------------|
| `GET` | `/audits/` | Lista eventos de auditoría (paginado). |

## Query params

| Parámetro | Descripción |
|-----------|-------------|
| `page` | Número de página. |
| `page_size` | `10`, `20` o `50`. |
| `search` | Busca en el campo `message` (icontains). |
| `order` | `asc` o `desc` por `created_at`. |
| `action` | Filtra por `LOGIN`, `LOGOUT`, `REGISTER`, `CREATE`, `UPDATE`, `DELETE`. |
| `session_state` | `ACTIVE` o `INACTIVE` (eventos de sesión). |

## Respuesta

Cada ítem incluye entre otros: `id`, `user_id`, `user_email`, `action`, `message`, `entity_type`, `entity_id`, `entity_name`, `session_state`, `session_started_at`, `session_ended_at`, **`ip_address`**, `created_at`.

Detalle en `Consumo Apis.md` (sección Audit).
