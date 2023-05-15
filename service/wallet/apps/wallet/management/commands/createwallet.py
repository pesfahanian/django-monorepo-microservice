from django.core.management.base import (
    BaseCommand,
    CommandError,
    CommandParser,
)

from apps.wallet.models import Wallet


class Command(BaseCommand):

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument(
            'user_id',
            type=str,
            help='User ID',
        )

    def handle(self, *args, **kwargs) -> None:
        try:
            Wallet.objects.get_or_create(user_id=kwargs['user_id'])

        except Exception as e:
            raise CommandError(f'Failure in `createwallet` command. '
                               f'Reason: {str(e)}.')
