from django.shortcuts import render
from django.http import HttpResponse
from .models import book_store

# Create your views here.
def index(request):
	my_function = book_store.objects.filter(book_name = 'book')
	return HttpResponse(my_function.order_by('publishing_length'))

