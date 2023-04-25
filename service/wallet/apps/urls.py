from django.urls import path, include

urlpatterns = [
    path(
        'healthcheck/',
        include('health_check.urls'),
    ),
]
