from django.urls import path

from .views import (
    document_type_detail_view,
    document_type_list_create_view,
    document_type_list_inactive_view,
)

urlpatterns = [
    path("document-types/", document_type_list_create_view, name="document-type-list-create"),
    path("document-types/inactive/", document_type_list_inactive_view, name="document-type-list-inactive"),
    path("document-types/<int:document_type_id>/", document_type_detail_view, name="document-type-detail"),
]
