from django.urls import path, include

urlpatterns = [
    path(
        'healthcheck/',
        include('health_check.urls'),
    ),
    path(
        'transactions/',
        include('apps.transaction.api.urls'),
    ),
    path(
        '',
        include('apps.wallet.api.urls'),
    ),
]
