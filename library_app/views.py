from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest
from .forms import NewAuthor, NewArticle
from library_app.models import ArticleModel, Comment


def all_article(request: HttpRequest, author):
    article = ArticleModel.objects.filter(author=author)
    return render(request, 'library_app/blog.html', {'articles': article})


def article_page(request: HttpRequest, article_id):
    article = get_object_or_404(ArticleModel, pk=article_id)
    article.view_count += 1
    article.save()
    # comments = Comment.object.filter(article=article)
    return render(request, 'library_app/article.html', {'article': article})


def new_author(request):
    if request.method == 'POST':
        form = NewAuthor(request.POST)
        if form.is_valid():
            author = form.save()
            return all_article(request, author.pk)
        else:
            return render(request, 'library_app/new_author.html', {'form': form})
    return render(request, 'library_app/new_author.html', {'form': NewAuthor})


def new_article(request):
    if request.method == 'POST':
        form = NewArticle(request.POST)
        if form.is_valid():
            article = form.save()
            return article_page(request, article.pk)
        else:
            return render(request, 'library_app/new_article.html', {'form': form})
    return render(request, 'library_app/new_article.html', {'form': NewArticle})












