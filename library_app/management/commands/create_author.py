from django.core.management.base import BaseCommand
from django.utils import lorem_ipsum
from library_app.models import AuthorModel


class Command(BaseCommand):
    help = "Create author."

    def handle(self, *args, **kwargs):
        for i in range(0, 5):
            author = AuthorModel(
                first_name=f'Name_{i}',
                last_name=f'Last_name_{i}',
                email=f'author{i}@gmail.com',
                bio=lorem_ipsum.words(10),
                dob='2000-11-12'
            )
            author.save()
        self.stdout.write(f'{author}')
