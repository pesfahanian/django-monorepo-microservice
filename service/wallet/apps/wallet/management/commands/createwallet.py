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
            user_id = kwargs['user_id']
            self.stdout.write(self.style.SUCCESS(f'UserID: {user_id}'))
            confirmation = input('Create wallet for this user ID? (yes/no): ')
            if (confirmation.lower() == 'yes'):
                Wallet.objects.get_or_create(user_id=user_id)

        except Exception as e:
            raise CommandError(f'Failure in `createwallet` command. '
                               f'Reason: {str(e)}.')
