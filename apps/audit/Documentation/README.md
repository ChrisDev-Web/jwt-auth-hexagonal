# Módulo `audit`

## Para qué sirve esta carpeta

La app `audit` centraliza el **registro de eventos** relevantes para trazabilidad y cumplimiento: inicios y cierres de sesión, altas de usuario y acciones sobre datos de negocio (por ejemplo CRUD en `document_types`).

Cada evento guarda **quién** (usuario), **qué** (acción y mensaje legible para el frontend), **sobre qué entidad** (tipo, id, nombre) y **desde qué IP** (incluyendo proxies vía `X-Forwarded-For` / `X-Real-IP`).

## Qué hace en la práctica

| Origen | Eventos típicos |
|--------|-----------------|
| `users` | `LOGIN`, `REGISTER`, cierre de sesión (actualización del evento LOGIN o `LOGOUT`). |
| `document_types` | `CREATE`, `UPDATE`, `DELETE` con mensajes “disfrazados” para UI. |

La **consulta** de auditoría es un endpoint protegido que devuelve listados paginados con filtros opcionales.

## Relación con otras apps

- No define la lógica de login/registro: solo **persiste** lo que otros módulos registran mediante `audit_logger`.
- Depende del modelo de usuario de Django (`AUTH_USER_MODEL`).

## Documentación adicional en esta carpeta

| Archivo | Contenido |
|---------|-----------|
| [estructura.md](./estructura.md) | Árbol de carpetas y capas. |
| [api.md](./api.md) | Endpoint de listado y filtros. |
| [eventos.md](./eventos.md) | Tipos de acción y campos del modelo. |

Ejemplos JSON: `Consumo Apis.md` en la raíz del proyecto.
