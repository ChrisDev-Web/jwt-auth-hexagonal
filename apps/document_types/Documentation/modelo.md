# Modelo `DocumentTypeModel`

Tabla: `document_types` (definida en `infrastructure/db/models.py`).

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `id` | BigAutoField | Identificador. |
| `name` | string | Nombre del tipo (indexado). |
| `description` | text | Texto libre. |
| `is_active` | boolean | Si el registro está vigente para uso normal. |
| `deleted_at` | datetime, nullable | Marca temporal de baja lógica. |
| `created_at` | datetime | Alta. |
| `updated_at` | datetime | Última modificación. |

## Regla de `deleted_at`

En `save()` del modelo:

- Si `is_active=True` → `deleted_at` se limpia (`None`).
- Si `is_active=False` y `deleted_at` estaba vacío → se asigna la fecha/hora actual.

Así el DELETE por API deja trazabilidad sin borrar la fila.
