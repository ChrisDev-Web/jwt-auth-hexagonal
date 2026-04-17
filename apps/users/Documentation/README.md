# Módulo `users`

## Para qué sirve esta carpeta

La app `users` es el **punto de entrada de identidad** del sistema: registro de cuentas, inicio y cierre de sesión, y la persistencia de **tokens** y **sesiones** asociados al usuario autenticado.

En una arquitectura hexagonal, `users` concentra:

- **Dominio**: entidades y contratos (repositorios) del usuario y autenticación.
- **Aplicación**: casos de uso (`LoginUser`, `RegisterUser`, `LogoutUser`) y DTOs.
- **Infraestructura**: modelos Django (`UserModel`, tokens, sesiones), repositorios concretos y autenticación JWT respaldada por base de datos.
- **Interfaces**: vistas API REST bajo el prefijo `/api/` (login, registro, logout).

## Qué hace en la práctica

| Función | Descripción |
|--------|-------------|
| Registro | Crea usuarios (según tu lógica actual de privilegios en el caso de uso). |
| Login | Valida credenciales, emite JWT (`access` / `refresh`), guarda hashes de tokens y abre sesión. |
| Logout | Recibe el `refresh`, revoca tokens del usuario en BD y cierra la sesión activa. |

Los endpoints públicos (`login`, `register`, `logout`) están marcados con `AllowAny`; el resto del proyecto usa por defecto `IsAuthenticated` y JWT validado también contra las tablas de tokens (revocación real del `access` tras logout).

## Relación con otras apps

- **audit**: los eventos de login, registro y logout disparan registros de auditoría (IP, mensajes, etc.).
- **document_types** y demás APIs protegidas: consumen el `access` emitido aquí.

## Documentación adicional en esta carpeta

| Archivo | Contenido |
|---------|-----------|
| [estructura.md](./estructura.md) | Árbol de carpetas y rol de cada capa hexagonal. |
| [api.md](./api.md) | Endpoints, método HTTP y notas de uso. |

Para ejemplos JSON detallados y `BASE URL`, ver también en la raíz del proyecto: `Consumo Apis.md`.
