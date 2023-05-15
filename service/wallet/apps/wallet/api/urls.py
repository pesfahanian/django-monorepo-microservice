from django.urls import path

from apps.wallet.api import views

urlpatterns = [
    path(
        '',
        views.GetWalletAPIView.as_view(),
    ),
]
