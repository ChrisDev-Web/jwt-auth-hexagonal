# API del módulo `document_types`

**Base URL**: `http://127.0.0.1:8000/api`

**Autenticación**: `Authorization: Bearer <access_token>`

## Endpoints

| Método | Ruta | Descripción |
|--------|------|-------------|
| `GET` | `/document-types/` | Lista **activos** (`is_active=True`). |
| `POST` | `/document-types/` | Crea un tipo de documento. |
| `GET` | `/document-types/inactive/` | Lista **inactivos**. |
| `GET` | `/document-types/<id>/` | Detalle por id. |
| `PUT` | `/document-types/<id>/` | Actualiza. |
| `DELETE` | `/document-types/<id>/` | Baja lógica (`is_active=False`, `deleted_at`). |

## Query params (GET listados)

| Parámetro | Valores | Descripción |
|-----------|---------|-------------|
| `page` | entero | Página (por defecto 1). |
| `page_size` | `10`, `20`, `50` | Tamaño de página. |
| `search` | texto | Filtra por nombre (icontains). |
| `order` | `asc` / `desc` | Orden por `created_at`. |

## Respuesta estándar

Ver sección Document Types en `Consumo Apis.md` (raíz del proyecto).
