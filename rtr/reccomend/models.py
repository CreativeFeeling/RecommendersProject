from django.db import models

class ClothingItem(models.Model):
    item_id = models.IntegerField(blank=True, null=True)
    event_type = models.CharField(max_length=50)

class Ratings(models.Model):
    item_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    colthing_bust = models.IntegerField(blank=True, null=True)
    colthing_size = models.CharField(max_length=50)
    body_shape = models.CharField(max_length=50)
    rating_val = models.IntegerField(blank=True, null=True)
    rating_text = models.CharField(max_length=200)

class User(models.Model):
    user_id = models.IntegerField(blank=True, null=True)
    colthing_bust = models.IntegerField(blank=True, null=True)
    colthing_size = models.CharField(max_length=50)
    body_shape = models.CharField(max_length=50)
