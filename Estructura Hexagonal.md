# Estructura Hexagonal del Proyecto

## Raiz

```text
Autenticacion/
├── .env
├── .env.example
├── Estructura Hexagonal.md
├── Consumo Apis.md
├── manage.py
├── requirements.txt
├── security.log
├── config/
└── apps/
```

## Config

```text
config/
├── __init__.py
├── asgi.py
├── settings.py
├── urls.py
└── wsgi.py
```

## Apps

```text
apps/
├── users/
├── document_types/
└── audit/
```

## App Users (Hexagonal)

```text
apps/users/
├── apps.py
├── models.py
├── documentation/
│   ├── README.md
│   ├── estructura.md
│   └── api.md
├── migrations/
│   ├── 0001_initial.py
│   └── 0002_usersessionmodel_ended_at.py
├── domain/
│   ├── entities/
│   │   └── user.py
│   ├── exceptions/
│   │   └── auth_exceptions.py
│   └── repositories/
│       ├── session_repository.py
│       ├── token_repository.py
│       └── user_repository.py
├── application/
│   ├── dto/
│   │   ├── login_dto.py
│   │   └── register_dto.py
│   └── use_cases/
│       ├── login_user.py
│       ├── logout_user.py
│       └── register_user.py
├── infrastructure/
│   ├── authentication.py
│   ├── db/
│   │   └── models.py
│   ├── repositories/
│   │   ├── django_session_repository.py
│   │   ├── django_token_repository.py
│   │   └── django_user_repository.py
│   └── serializers/
│       └── user_serializer.py
└── interfaces/
    └── api/
        ├── urls.py
        └── views.py
```

## App Document Types (Hexagonal)

```text
apps/document_types/
├── __init__.py
├── apps.py
├── models.py
├── documentation/
│   ├── README.md
│   ├── estructura.md
│   ├── api.md
│   └── modelo.md
├── migrations/
│   ├── __init__.py
│   ├── 0001_initial.py
│   └── 0002_remove_code_add_deleted_at.py
├── domain/
│   ├── __init__.py
│   ├── entities/
│   │   ├── __init__.py
│   │   └── document_type.py
│   ├── exceptions/
│   │   ├── __init__.py
│   │   └── document_type_exceptions.py
│   └── repositories/
│       ├── __init__.py
│       └── document_type_repository.py
├── application/
│   ├── __init__.py
│   ├── dto/
│   │   ├── __init__.py
│   │   ├── create_document_type_dto.py
│   │   └── update_document_type_dto.py
│   └── use_cases/
│       ├── __init__.py
│       ├── create_document_type.py
│       ├── delete_document_type.py
│       ├── get_document_type.py
│       ├── list_document_types.py
│       └── update_document_type.py
├── infrastructure/
│   ├── __init__.py
│   ├── db/
│   │   ├── __init__.py
│   │   └── models.py
│   ├── repositories/
│   │   ├── __init__.py
│   │   └── django_document_type_repository.py
│   └── serializers/
│       ├── __init__.py
│       └── document_type_serializer.py
└── interfaces/
    ├── __init__.py
    └── api/
        ├── __init__.py
        ├── urls.py
        └── views.py
```

## App Audit (Hexagonal)

```text
apps/audit/
├── __init__.py
├── apps.py
├── models.py
├── documentation/
│   ├── README.md
│   ├── estructura.md
│   ├── api.md
│   └── eventos.md
├── migrations/
│   ├── __init__.py
│   ├── 0001_initial.py
│   └── 0002_auditeventmodel_ip_address.py
├── domain/
│   ├── __init__.py
│   ├── entities/
│   │   ├── __init__.py
│   │   └── audit_event.py
│   └── repositories/
│       ├── __init__.py
│       └── audit_repository.py
├── application/
│   ├── __init__.py
│   └── use_cases/
│       ├── __init__.py
│       └── list_audits.py
├── infrastructure/
│   ├── __init__.py
│   ├── db/
│   │   ├── __init__.py
│   │   └── models.py
│   ├── repositories/
│   │   ├── __init__.py
│   │   └── django_audit_repository.py
│   ├── serializers/
│   │   ├── __init__.py
│   │   └── audit_serializer.py
│   └── services/
│       ├── __init__.py
│       ├── audit_logger.py
│       └── ip_resolver.py
└── interfaces/
    ├── __init__.py
    └── api/
        ├── __init__.py
        ├── urls.py
        └── views.py
```
