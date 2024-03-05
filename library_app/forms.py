from django import forms
from library_app.models import AuthorModel, ArticleModel


class NewAuthor(forms.ModelForm):
    class Meta:
        model = AuthorModel
        fields = ['first_name', 'last_name', 'email', 'bio', 'dob']


class NewArticle(forms.ModelForm):
    class Meta:
        model = ArticleModel
        fields = ['title', 'text', 'author', 'category', 'public_flag']
