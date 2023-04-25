from django.contrib import admin
from django.urls import path
from django.urls.conf import include

from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title='DMM-Wallet Service',
        default_version='0.1.0',
        description='Swagger UI for DMM-Wallet service API schema.',
    ),
    permission_classes=[
        permissions.AllowAny,
    ],
    public=True,
)

urlpatterns = [
    path(
        'admin/',
        admin.site.urls,
    ),
    path(
        'swagger/',
        schema_view.with_ui(
            'swagger',
            cache_timeout=0,
        ),
        name='api-schema-swagger-ui',
    ),
    path(
        'api/v1/wallet/',
        include('apps.urls'),
    ),
]
