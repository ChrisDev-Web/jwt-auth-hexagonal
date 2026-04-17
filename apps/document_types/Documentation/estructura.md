# Estructura hexagonal del módulo `document_types`

```
apps/document_types/
├── apps.py
├── models.py               # Re-export desde infrastructure/db/models
├── migrations/             # Esquema inicial + eliminación de code + deleted_at
├── domain/
│   ├── entities/           # Entidad de dominio DocumentType
│   ├── exceptions/         # Ej. DocumentTypeNotFound
│   └── repositories/       # Contrato DocumentTypeRepository
├── application/
│   ├── dto/                # CreateDocumentTypeDTO, UpdateDocumentTypeDTO
│   └── use_cases/          # Create, List, Get, Update, Delete (soft)
├── infrastructure/
│   ├── db/models.py        # DocumentTypeModel (tabla document_types)
│   ├── repositories/       # DjangoDocumentTypeRepository
│   └── serializers/        # Serializers de entrada/salida DRF
└── interfaces/api/
    ├── urls.py
    └── views.py            # Paginación, search, order, respuesta estandarizada
```

## Flujo

1. La vista valida con serializers DRF.
2. Los casos de uso orquestan reglas de negocio y llaman al repositorio Django.
3. El repositorio persiste en `DocumentTypeModel`; el delete actualiza `is_active` y el modelo ajusta `deleted_at` en `save()`.
