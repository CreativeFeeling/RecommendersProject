# Generated by Django 2.1.5 on 2019-04-23 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reccomend', '0002_clothingitem_colthing_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='clothingitem',
            name='item_id',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ratings',
            name='item_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]