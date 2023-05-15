from django.urls import path

from apps.wallet.api import views

urlpatterns = [
    path(
        '',
        views.WalletGetAPIView.as_view(),
    ),
]
