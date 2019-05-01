from django.db import models

class ClothingItem(models.Model):
    item_id = models.IntegerField(blank=True,primary_key=True)
    event_type = models.CharField(max_length=50)
    avg_rating = models.IntegerField(blank=True, null=True)
    img_url = models.CharField(max_length=200)

class User(models.Model):
    user_id = models.IntegerField(blank=True, primary_key=True)
    colthing_bust = models.CharField(max_length=5)
    colthing_size = models.CharField(max_length=50)
    body_shape = models.CharField(max_length=50)

class Rating(models.Model):
    item_id = models.ForeignKey(ClothingItem, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    colthing_bust = models.IntegerField(blank=True, null=True)
    colthing_size = models.CharField(max_length=50)
    body_shape = models.CharField(max_length=50)
    rating_val = models.IntegerField(blank=True, null=True)
    rating_text = models.CharField(max_length=200)

class Event(models.Model):
    event_name = models.CharField(max_length=50)
    img_url = models.CharField(max_length=200)
