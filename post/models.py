from django.db import models
from author.models import Author

# Create your models here.


class PostCategory(models.Model):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=100, unique=True)
    content = models.CharField(max_length=2500)
    publication_date = models.DateTimeField()
    post_category = models.ForeignKey(PostCategory, related_name='', on_delete=models.CASCADE)
    author = models.ForeignKey(Author,related_name='',on_delete=models.CASCADE)
