from django.core.management.base import BaseCommand
from django.utils import lorem_ipsum

from hw_2_app.models import User


class Command(BaseCommand):
    help = "Create user."

    def handle(self, *args, **kwargs):
        for i in range(0, 5):
            new_user = User(
                name=f'name_{1}',
                email=f'author{i}@gmail.com',
                phone_number=f'123456789{i}',
                address=lorem_ipsum.words(10)
            )
            new_user.save()
        self.stdout.write(f'{new_user}')