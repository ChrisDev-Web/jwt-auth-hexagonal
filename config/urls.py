from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('apps.users.interfaces.api.urls')),
    path('api/', include('apps.document_types.interfaces.api.urls')),
    path('api/', include('apps.audit.interfaces.api.urls')),
]