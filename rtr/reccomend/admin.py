from django.contrib import admin
from .models import ClothingItem, Rating, User

admin.site.register(ClothingItem)
admin.site.register(Rating)
admin.site.register(User)
