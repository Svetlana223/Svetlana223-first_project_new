from django.contrib import admin
from .models import AuthorModel, ArticleModel, Comment


@admin.register(AuthorModel)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'dob', 'email']
    # readonly_fields = ['date_of_public', 'view_count']
    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['full_name'],
            },
        ),
        (
            'Подробности',
            {
                'classes': ['collapse'],
                'description': 'Биография', 'fields': ['bio'],
            },
        ),
        (
            'Дата рождения',
            {
                'fields': ['dob'],
            }
        ),
        (
            'Контакты',
            {
                'fields': ['email'],
            }
        ),
    ]


@admin.register(ArticleModel)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['author', 'title', 'category']
    readonly_fields = ['date_of_public', 'view_count']

    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['author'],
            },
        ),
        (
            'Подробности',
            {
                'classes': ['collapse'],
                'description': 'Текст статьи', 'fields': ['title', 'text'],
            },
        ),
        (
            'Категория и дата публикации',
            {
                'fields': ['category', 'date_of_public'],
            }
        ),
        (
            'Число просмотров и статус',
            {
                'description': 'Статистика просмотров',
                'fields': ['view_count', 'public_flag'],
            }
        ),
    ]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['author', 'article', 'text', 'date_of_public']

