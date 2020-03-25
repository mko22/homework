from django.db import models

# Create your models here.
class Album(models.Model):
	album_name = models.CharField(max_length = 200)

class Song(models.Model):
	my_var = models.ForeignKey(Album, on_delete=models.CASCADE)
	song_name = models.CharField(max_length = 50)
	duration = models.IntegerField(default=0)


