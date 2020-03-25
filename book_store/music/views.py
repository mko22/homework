from django.shortcuts import render
from django.http import HttpResponse
from .models import Album, Song

# Create your views here.
def count(request, album_id):
	my_list = []
	my_album = Album.objects.get(pk=album_id)
	my_songs = Song.objects.filter(my_var = album_id)
	for song in my_songs:
		my_list.append('<br>' + song.song_name + ' ' + str(song.duration))
	return HttpResponse(my_album.album_name + ''.join(my_list))

def dambldor(request):
	return HttpResponse("What's up Jirayr???")

