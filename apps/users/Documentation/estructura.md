# Estructura hexagonal del módulo `users`

```
apps/users/
├── apps.py                 # Configuración de la app Django
├── models.py               # Re-export de modelos desde infrastructure/db
├── migrations/             # Migraciones de UserModel, tokens, sesiones
├── domain/                 # Núcleo de negocio (independiente de Django)
│   ├── entities/           # Entidad User (dominio)
│   ├── exceptions/         # Excepciones (credenciales inválidas, usuario duplicado, etc.)
│   └── repositories/       # Interfaces abstractas de repositorios
├── application/            # Casos de uso y DTOs
│   ├── dto/                # LoginDTO, RegisterDTO
│   └── use_cases/          # LoginUser, RegisterUser, LogoutUser
├── infrastructure/         # Implementación técnica
│   ├── db/models.py        # UserModel (AbstractUser), AccessToken, RefreshToken, UserSession
│   ├── repositories/       # DjangoUserRepository, DjangoTokenRepository, DjangoSessionRepository
│   ├── serializers/      # LoginSerializer, RegisterSerializer, LogoutSerializer
│   └── authentication.py   # JWT + comprobación en BD (token revocado / vigente)
└── interfaces/api/         # Entrada HTTP
    ├── urls.py             # Rutas login, register, logout
    └── views.py            # Vistas y respuesta estandarizada (message, data, error)
```

## Flujo de datos (resumen)

1. **Request** llega a `interfaces/api/views.py`.
2. El serializer valida el cuerpo; se construye un **DTO** y se invoca el **caso de uso**.
3. El caso de uso usa **repositorios** de infraestructura para leer/escribir en BD y emitir JWT.
4. La respuesta se envuelve en el formato común del proyecto (`message`, `data`, `pagination`, `error`).

## Convenciones

- Los secretos y la configuración global están en `config/settings.py` (no en esta app).
- La revocación de tokens tras logout afecta a los `access` guardados en BD para ese usuario.
