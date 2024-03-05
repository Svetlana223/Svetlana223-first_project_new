from django.core.management.base import BaseCommand
from django.utils import lorem_ipsum
from library_app.models import AuthorModel, ArticleModel
from random import choice


class Command(BaseCommand):
    help = "Create article."

    def handle(self, *args, **kwargs):
        authors = AuthorModel.objects.all()
        for i in range(0, 5):
            article = ArticleModel(
                author=choice(authors),
                title=f'Article #{i}',
                text=lorem_ipsum.paragraphs(4),
                category=f'Category {i}'
            )
            article.save()
        self.stdout.write(f'{article}')

