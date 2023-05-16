from django.conf import settings
from django.core.management.base import (
    BaseCommand,
    CommandError,
    CommandParser,
)
from rest_framework_simplejwt.tokens import RefreshToken

from apps.wallet.models import Wallet

settings.SIMPLE_JWT['SIGNING_KEY'] = open(
    f'{settings.REPO_DIR}/keys/jwtRS256.key').read()


class User:

    def __init__(self, user_id: str) -> None:
        self.user_id = user_id


class Command(BaseCommand):

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument(
            'user_id',
            type=str,
            help='User ID',
        )

    def handle(self, *args, **kwargs) -> None:
        try:
            user_id = kwargs['user_id']

            if not Wallet.objects.filter(user_id=user_id).exists():
                raise Exception(
                    f'Wallet for user with ID `{user_id}` does not exist.')

            token = str(
                RefreshToken.for_user(user=User(user_id=user_id)).access_token)

            self.stdout.write(self.style.SUCCESS(f'Access Token: {token}'))

            while True:
                confirmation = input('Exit? (yes/no): ')
                if (confirmation.lower() == 'yes'):
                    break

        except Exception as e:
            raise CommandError(f'Failure in `generatetoken` command. '
                               f'Reason: {str(e)}.')
