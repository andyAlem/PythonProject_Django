from django.core.management import call_command
from django.core.management.base import BaseCommand

from catalog.models import Category, Product


class Command(BaseCommand):
    help = "Удаляет все продукты и категории, и импортирует фикстуру catalog.json"

    def handle(self, *args, **kwargs):
        Category.objects.all().delete()
        Product.objects.all().delete()

        call_command("loaddata", "catalog.json")
        self.stdout.write(self.style.SUCCESS("Категории и товары успешно загружены"))
