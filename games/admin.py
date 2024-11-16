from django.utils.html import format_html
from django.contrib import admin
from .models import Game, Item

class GameAdmin(admin.ModelAdmin):
    list_display = ('name', 'emojie', 'image_tag')
    search_fields = ('name', 'description')

    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 50px; height:50px;" />'.format(obj.image.url))
        return "No Image"

    image_tag.short_description = 'image'

class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', "emojie_1", 'image_tag', 'price_', 'emojie_2', 'category')
    search_fields = ('name', 'description')

    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 50px; height:50px;" />'.format(obj.image.url))
        return "No Image"

    def price_(self, obj):
        return obj.price + " هزارتومن"

    image_tag.short_description = 'image'


admin.site.register(Game, GameAdmin)
admin.site.register(Item, ItemAdmin)

