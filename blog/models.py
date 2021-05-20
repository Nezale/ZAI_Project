from django.db import models

# Create your models here.


class Author(models.Model):
    nickname = models.CharField(max_length=50, unique=True)
    firstname = models.CharField(max_length=50, unique=False)
    lastname = models.CharField(max_length=50, unique=False)
    birthday = models.DateField()
    about = models.CharField(max_length=500)

    class Meta:
        ordering = ('nickname',)

    def __str__(self):
        return self.nickname


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
    post_category = models.ForeignKey(PostCategory, on_delete=models.CASCADE)
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
