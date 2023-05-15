from django.urls import path

from apps.transaction.api import views

urlpatterns = [
    path(
        '',
        views.TransactionListCreateAPIView.as_view(),
    ),
]
