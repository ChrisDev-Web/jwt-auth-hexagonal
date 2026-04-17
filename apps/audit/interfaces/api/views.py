import logging
import traceback
from django.core.paginator import EmptyPage, Paginator
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from apps.audit.application.use_cases.list_audits import ListAudits
from apps.audit.infrastructure.repositories.django_audit_repository import DjangoAuditRepository

logger = logging.getLogger(__name__)


def _ok(data=None, message="OK", pagination=None):
    return {"message": message, "data": data if data is not None else {}, "pagination": pagination, "error": None}


def _fail(message, detail=None):
    return {"message": message, "data": {}, "pagination": None, "error": detail if detail is not None else message}


def _to_output(item):
    return {
        "id": item.id,
        "user_id": item.user_id,
        "user_email": item.user.email if item.user else "",
        "action": item.action,
        "message": item.message,
        "entity_type": item.entity_type,
        "entity_id": item.entity_id,
        "entity_name": item.entity_name,
        "session_state": item.session_state,
        "session_started_at": item.session_started_at,
        "session_ended_at": item.session_ended_at,
        "ip_address": item.ip_address,
        "created_at": item.created_at,
    }


def _paginate(request, queryset):
    page = int(request.query_params.get("page", 1))
    page_size = int(request.query_params.get("page_size", 10))
    if page_size not in (10, 20, 50):
        page_size = 10

    paginator = Paginator(queryset, page_size)
    try:
        page_obj = paginator.page(page)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages if paginator.num_pages > 0 else 1)

    return _ok(
        data={"items": [_to_output(item) for item in page_obj.object_list]},
        message="Auditoria obtenida",
        pagination={
            "page": page_obj.number,
            "page_size": page_size,
            "total_items": paginator.count,
            "total_pages": paginator.num_pages,
            "has_next": page_obj.has_next(),
            "has_previous": page_obj.has_previous(),
        },
    )


@api_view(["GET"])
def audit_list_view(request):
    try:
        action = request.query_params.get("action")
        session_state = request.query_params.get("session_state")
        search = request.query_params.get("search")
        order = request.query_params.get("order", "desc").lower()
        queryset = ListAudits(DjangoAuditRepository()).execute(
            action=action,
            session_state=session_state,
        )
        if search:
            queryset = queryset.filter(message__icontains=search)
        queryset = queryset.order_by("created_at" if order == "asc" else "-created_at")
        payload = _paginate(request, queryset)
        return Response(payload, status=status.HTTP_200_OK)

    except Exception as e:
        logger.error(traceback.format_exc())
        return Response(_fail("Internal server error", str(e)), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
