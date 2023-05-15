from uuid import uuid4

from django.core.management import call_command
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):

    def handle(self, *args, **kwargs) -> None:
        try:
            call_command(
                'createwallet',
                str(uuid4()),
            )

        except Exception as e:
            raise CommandError(f'Failure in `seed` command. '
                               f'Reason: {str(e)}.')
