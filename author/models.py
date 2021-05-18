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
