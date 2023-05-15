from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):

    def handle(self, *args, **kwargs) -> None:
        try:
            pass

        except Exception as e:
            raise CommandError(f'Failure in `seed` command. '
                               f'Reason: {str(e)}.')
