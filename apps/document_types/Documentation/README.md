# Módulo `document_types`

## Para qué sirve esta carpeta

La app `document_types` gestiona el **catálogo de tipos de documento** del sistema (por ejemplo DNI, pasaporte): nombre, descripción, estado activo/inactivo y **borrado lógico** con `deleted_at`.

Es un módulo **protegido**: todas las operaciones (salvo que cambies permisos) requieren usuario autenticado y JWT válido (`Authorization: Bearer <access>`).

## Qué hace en la práctica

| Función | Descripción |
|--------|-------------|
| Listar activos | Solo registros con `is_active=True`, con paginación, búsqueda y orden. |
| Listar inactivos | Solo `is_active=False` (incluye los dados de baja lógica). |
| CRUD | Crear, leer uno, actualizar; el **DELETE** es soft delete (marca inactivo y `deleted_at`). |

Las respuestas siguen el formato estándar del proyecto: `message`, `data`, `pagination`, `error`.

## Relación con otras apps

- **audit**: cada alta, edición o baja genera un evento de auditoría con mensaje orientado al frontend y **IP** del cliente.
- **users**: el usuario autenticado es quien ejecuta las acciones registradas en auditoría.

## Documentación adicional en esta carpeta

| Archivo | Contenido |
|---------|-----------|
| [estructura.md](./estructura.md) | Árbol de carpetas y capas hexagonales. |
| [api.md](./api.md) | Endpoints, query params y notas. |
| [modelo.md](./modelo.md) | Campos del modelo y reglas de `deleted_at`. |

Para JSON de ejemplo: `Consumo Apis.md` en la raíz del proyecto.
