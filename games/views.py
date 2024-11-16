from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics

from .models import Game
from .models import Item
from .serializers import GameSerializer
from .serializers import ItemSerializer


class ItemListView(ListAPIView):
    serializer_class = ItemSerializer
    def get_queryset(self):
        queryset = Item.objects.all()
        game_id = self.request.query_params.get('game')
        if game_id is not None:
            queryset = queryset.filter(game__id=game_id)
        return queryset

@api_view(['GET'])
def game_list(request):
    games = Game.objects.all()
    serializer = GameSerializer(games, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def item_list(request, pk):
    items = Item.objects.all().filter(category__id=pk)
    category = Game.objects.get(id=pk)
    serializer = ItemSerializer(items, many=True)
    return Response({"game": {"name": category.name,"dis":  category.description},
                     "items": serializer.data})


