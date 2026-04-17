from django.urls import path

from .views import audit_list_view

urlpatterns = [
    path("audits/", audit_list_view, name="audit-list"),
]
