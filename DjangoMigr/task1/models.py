from django.db import models
class Buyer(models.Model):
    name = models.CharField(max_length=50)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    age = models.DecimalField(max_digits=3, decimal_places=0)


class Game(models.Model):
    title = models.CharField(max_length=100)
    cost = models.DecimalField(max_digits=7, decimal_places=2)
    size = models.DecimalField(max_digits=9, decimal_places=0)
    description = models.TextField()
    age_limited = models.BooleanField(default=False)
    buyer = models.ManyToManyField(Buyer,related_name='gamebuyers')

class Post(models.Model):
    title = models.CharField(max_length=100,verbose_name='Заголовок поста')
    content = models.TextField(verbose_name='Содержание поста')
    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Пост'
# Create your models here.
