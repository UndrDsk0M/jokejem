from django.urls import path
from .views import game_list, item_list

urlpatterns = [
    path('games/', game_list, name='game-list'),
    path('items/<int:pk>', item_list, name='items'),
]
