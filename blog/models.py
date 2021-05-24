from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    about = models.CharField(max_length=500)

    def __str__(self):
        return self.user.get_username()


@receiver(post_save, sender=User)
def create_author(sender, instance, created, **kwargs):
    if created:
        Author.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_author(sender, instance, **kwargs):
    instance.author.save()


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
    post_category = models.ForeignKey(PostCategory, related_name='posts', on_delete=models.CASCADE)
    author = models.ForeignKey(Author, related_name='author', on_delete=models.CASCADE)
