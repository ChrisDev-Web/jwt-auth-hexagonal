import logging
import traceback
from django.core.paginator import EmptyPage, Paginator

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from apps.document_types.application.dto.create_document_type_dto import CreateDocumentTypeDTO
from apps.document_types.application.dto.update_document_type_dto import UpdateDocumentTypeDTO
from apps.document_types.application.use_cases.create_document_type import CreateDocumentType
from apps.document_types.application.use_cases.delete_document_type import DeleteDocumentType
from apps.document_types.application.use_cases.get_document_type import GetDocumentType
from apps.document_types.application.use_cases.list_document_types import ListDocumentTypes
from apps.document_types.application.use_cases.update_document_type import UpdateDocumentType
from apps.document_types.domain.exceptions.document_type_exceptions import DocumentTypeNotFound
from apps.document_types.infrastructure.repositories.django_document_type_repository import DjangoDocumentTypeRepository
from apps.document_types.infrastructure.serializers.document_type_serializer import (
    CreateDocumentTypeSerializer,
    UpdateDocumentTypeSerializer,
)
from apps.audit.infrastructure.services.ip_resolver import get_client_ip

logger = logging.getLogger(__name__)


def _ok(data=None, message="OK", pagination=None):
    return {"message": message, "data": data if data is not None else {}, "pagination": pagination, "error": None}


def _fail(message, detail=None):
    return {"message": message, "data": {}, "pagination": None, "error": detail if detail is not None else message}


def _to_output(document_type):
    return {
        "id": document_type.id,
        "name": document_type.name,
        "description": document_type.description,
        "is_active": document_type.is_active,
        "deleted_at": document_type.deleted_at,
        "created_at": document_type.created_at,
        "updated_at": document_type.updated_at,
    }


def _apply_search_and_order(request, queryset):
    search = request.query_params.get("search")
    if search:
        queryset = queryset.filter(name__icontains=search)

    order = request.query_params.get("order", "desc").lower()
    return queryset.order_by("created_at" if order == "asc" else "-created_at")


def _build_paginated_response(request, queryset, serializer_fn, message):
    page = int(request.query_params.get("page", 1))
    page_size = int(request.query_params.get("page_size", 10))
    if page_size not in (10, 20, 50):
        page_size = 10

    queryset = _apply_search_and_order(request, queryset)
    paginator = Paginator(queryset, page_size)
    try:
        page_obj = paginator.page(page)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages if paginator.num_pages > 0 else 1)

    return _ok(
        data={"items": [serializer_fn(item) for item in page_obj.object_list]},
        message=message,
        pagination={
            "page": page_obj.number,
            "page_size": page_size,
            "total_items": paginator.count,
            "total_pages": paginator.num_pages,
            "has_next": page_obj.has_next(),
            "has_previous": page_obj.has_previous(),
        },
    )


@api_view(["GET", "POST"])
def document_type_list_create_view(request):
    repository = DjangoDocumentTypeRepository()
    try:
        if request.method == "GET":
            result = ListDocumentTypes(repository).execute(is_active=True)
            payload = _build_paginated_response(request, result, _to_output, "Registros activos obtenidos")
            return Response(payload, status=status.HTTP_200_OK)

        serializer = CreateDocumentTypeSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(_fail("Invalid data", serializer.errors), status=status.HTTP_400_BAD_REQUEST)

        dto = CreateDocumentTypeDTO(**serializer.validated_data)
        created = CreateDocumentType(repository).execute(dto)
        from apps.audit.infrastructure.services.audit_logger import log_record_action
        log_record_action(
            user=request.user,
            action="CREATE",
            entity_type="DocumentType",
            entity_id=created.id,
            entity_name=created.name,
            message="Creo registro en tipo de documento",
            ip_address=get_client_ip(request),
        )
        return Response(_ok(_to_output(created), "Registro creado"), status=status.HTTP_201_CREATED)

    except Exception as e:
        logger.error(traceback.format_exc())
        return Response(_fail("Internal server error", str(e)), status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["GET", "PUT", "DELETE"])
def document_type_detail_view(request, document_type_id):
    repository = DjangoDocumentTypeRepository()
    try:
        if request.method == "GET":
            result = GetDocumentType(repository).execute(document_type_id)
            return Response(_ok(_to_output(result), "Registro obtenido"), status=status.HTTP_200_OK)

        if request.method == "PUT":
            serializer = UpdateDocumentTypeSerializer(data=request.data)
            if not serializer.is_valid():
                return Response(_fail("Invalid data", serializer.errors), status=status.HTTP_400_BAD_REQUEST)

            dto = UpdateDocumentTypeDTO(**serializer.validated_data)
            updated = UpdateDocumentType(repository).execute(document_type_id, dto)
            from apps.audit.infrastructure.services.audit_logger import log_record_action
            log_record_action(
                user=request.user,
                action="UPDATE",
                entity_type="DocumentType",
                entity_id=updated.id,
                entity_name=updated.name,
                message="Edito registro en tipo de documento",
                ip_address=get_client_ip(request),
            )
            return Response(_ok(_to_output(updated), "Registro actualizado"), status=status.HTTP_200_OK)

        deleted = DeleteDocumentType(repository).execute(document_type_id)
        from apps.audit.infrastructure.services.audit_logger import log_record_action
        log_record_action(
            user=request.user,
            action="DELETE",
            entity_type="DocumentType",
            entity_id=deleted.id,
            entity_name=deleted.name,
            message="Elimino registro en tipo de documento",
            ip_address=get_client_ip(request),
        )
        return Response(
            _ok(
                {
                    "id": deleted.id,
                    "name": deleted.name,
                    "is_active": deleted.is_active,
                    "deleted_at": deleted.deleted_at,
                },
                "Registro eliminado",
            ),
            status=status.HTTP_200_OK,
        )

    except DocumentTypeNotFound:
        return Response(_fail("Document type not found"), status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        logger.error(traceback.format_exc())
        return Response(_fail("Internal server error", str(e)), status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["GET"])
def document_type_list_inactive_view(request):
    repository = DjangoDocumentTypeRepository()
    try:
        result = ListDocumentTypes(repository).execute(is_active=False)
        payload = _build_paginated_response(request, result, _to_output, "Registros inactivos obtenidos")
        return Response(payload, status=status.HTTP_200_OK)
    except Exception as e:
        logger.error(traceback.format_exc())
        return Response(_fail("Internal server error", str(e)), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
