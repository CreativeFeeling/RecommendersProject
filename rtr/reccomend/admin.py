from django.contrib import admin
from .models import ClothingItem, Rating, User, Event

admin.site.register(ClothingItem)
admin.site.register(Rating)
admin.site.register(User)
admin.site.register(Event)
