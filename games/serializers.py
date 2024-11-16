# serializers.py
from rest_framework import serializers
from .models import Game, Item

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ['id', 'emojie', 'name', 'description']

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['name', 'emojie_1', 'price', 'emojie_2', 'category']
