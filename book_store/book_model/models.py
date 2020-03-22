from django.db import models


# Create your models here.
class book_store(models.Model):
    book_name = models.CharField(max_length = 20)
    publishing_length = models.IntegerField()
    author_name = models.CharField(max_length = 20)
    book_genre = models.CharField(max_length = 20) 