import csv

from django.core.management.base import BaseCommand
from phones.models import Phone
from datetime import datetime

class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for phone in phones:
            release_date = datetime.strptime(phone['release_date'], '%Y-%m-%d').date()
            lte_exists = phone['lte_exists'].lower() == 'true'
            id = phone['id']
            Phone.objects.create(
                id=id,
                name = phone['name'],
                image = phone['image'],
                price = phone['price'],
                lte_exists = lte_exists,
                release_date = release_date
            )
        self.stdout.write(self.style.SUCCESS('Данные успешно импортированы!'))