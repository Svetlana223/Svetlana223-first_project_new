from django.db import models
from django.urls import reverse


class AuthorModel(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    bio = models.CharField(max_length=300)
    dob = models.DateField()
    full_name = models.CharField(blank=True, null=True, max_length=200)

    def save(self, *args, **kwargs):
        self.full_name = self.first_name + ' ' + self.last_name
        return super().save(*args, **kwargs)

    def __str__(self):
        return f'Username: {self.full_name}'


class ArticleModel(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    date_of_public = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(AuthorModel, on_delete=models.CASCADE)
    category = models.CharField(max_length=100)
    view_count = models.IntegerField(default=0)
    public_flag = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('article_page', kwargs={'article_id': self.pk})

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.ForeignKey(AuthorModel, on_delete=models.CASCADE)
    article = models.ForeignKey(ArticleModel, on_delete=models.CASCADE)
    text = models.TextField()
    date_of_public = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text
