from django.core.management.base import BaseCommand
from random import randint, choice, uniform, sample
from hw_2_app.models import Order, User, Product


class Command(BaseCommand):
    help = "Create order."

    def handle(self, *args, **kwargs):
        users = list(User.objects.all())
        products = list(Product.objects.all())

        for i in range(5):
            user = choice(users)
            order = Order.objects.create(
                user=user,
                total_amount=uniform(10.0, 100.0)
            )
            order.products.set(sample(products, k=randint(1, len(products))))
            order.save()
            self.stdout.write(f'Создание заказа {order.id}')
