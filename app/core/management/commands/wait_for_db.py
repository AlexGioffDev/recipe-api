"""
Django command to wait for the DB to be available
"""
from django.core.management.base import BaseCommand  # type: ignore
from psycopg2 import OperationalError as Psycopg2Error  # type: ignore
from django.db.utils import OperationalError  # type: ignore
import time


class Command(BaseCommand):
    """Django command to wait for database"""

    def handle(self, *args, **options):
        """Entrypoint for command"""
        self.stdout.write("Watigin for databse")
        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except (Psycopg2Error, OperationalError):
                self.stdout.write('Databse unavailabe, waiting 1 second')
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS('Database availabe'))
