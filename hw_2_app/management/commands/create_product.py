from django.core.management.base import BaseCommand
from django.utils import lorem_ipsum

from hw_2_app.models import Product


class Command(BaseCommand):
    help = "Create product."

    def handle(self, *args, **kwargs):
        for i in range(0, 5):
            new_product = Product(
                name=f'name{i}',
                description=lorem_ipsum.words(10),
                price=15.50,
                stock=f'{50 - i}'
            )
            new_product.save()
        self.stdout.write(f'{new_product}')
