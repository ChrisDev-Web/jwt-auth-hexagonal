# Estructura hexagonal del módulo `audit`

```
apps/audit/
├── apps.py
├── models.py               # Re-export desde infrastructure/db/models
├── migrations/             # AuditEventModel + ip_address
├── domain/
│   ├── entities/           # Entidad AuditEvent (dominio)
│   └── repositories/       # Contrato AuditRepository
├── application/
│   └── use_cases/          # ListAudits
├── infrastructure/
│   ├── db/models.py        # AuditEventModel → tabla audit_events
│   ├── repositories/     # DjangoAuditRepository
│   ├── serializers/      # Serializers de salida (opcional)
│   └── services/
│       ├── audit_logger.py # log_session_login, log_session_logout, log_user_registered, log_record_action
│       └── ip_resolver.py  # get_client_ip (proxy-safe)
└── interfaces/api/
    ├── urls.py
    └── views.py            # Listado paginado, search, order, filtros
```

## Flujo de escritura

1. Otras apps llaman funciones en `audit_logger` desde las vistas o casos de uso.
2. Se crea o actualiza `AuditEventModel` con `ip_address` cuando aplica.

## Flujo de lectura

1. `GET /api/audits/` usa `ListAudits` + `DjangoAuditRepository` y devuelve el formato estándar del proyecto.
