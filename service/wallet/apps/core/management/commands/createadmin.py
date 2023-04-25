from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):

    def handle(self, *args, **kwargs) -> None:
        try:
            User = get_user_model()
            if not User.objects.filter(
                    username=settings.ADMIN_USERNAME).exists():
                User.objects.create_user(
                    username=settings.ADMIN_USERNAME,
                    password=settings.ADMIN_PASSWORD,
                    is_staff=True,
                    is_active=True,
                    is_superuser=True,
                )

        except Exception as e:
            raise CommandError(f'Failure in `createadmin` command. '
                               f'Reason: {str(e)}.')
