from django.urls import path
from . import views

urlpatterns = [
    path('<int:album_id>/', views.count),
    path('grifindor/', views.dambldor),
]