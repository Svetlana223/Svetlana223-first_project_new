from django.urls import path
from . import views

urlpatterns = [
    path('blog/<int:author>/', views.all_article, name="all_article"),
    path('article/<int:article_id>/', views.article_page, name="article_page"),
    path('new_author/', views.new_author, name="new_author"),
    path('new_article/', views.new_article, name="new_article"),
]