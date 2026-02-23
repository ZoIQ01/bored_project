"""Management command for importing activities from the API."""

from django.core.management.base import BaseCommand, CommandError

from activities.services import import_activities
from activities.const import DEFAULT_IMPORT_TIMEOUT, MAX_IMPORT_COUNT

import requests



class Command(BaseCommand):
    """Run batch import of activities from the external endpoint."""
    help = "Import activity from Bored API"
    def handle(self, *args, **options):
        """Execute import and print a success or error summary."""
        try:
            added, skipped = import_activities(
                count=MAX_IMPORT_COUNT,
                timeout=DEFAULT_IMPORT_TIMEOUT,
            )
            self.stdout.write(self.style.SUCCESS(f'Successfully imported activities: {added} added, {skipped} skipped'))
        except requests.exceptions.Timeout:
            raise CommandError('Timeout occurred while importing activities')
        except Exception as e:
            raise CommandError(f'Error importing activities: {e}')