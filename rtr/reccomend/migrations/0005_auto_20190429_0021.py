# Generated by Django 2.1.5 on 2019-04-29 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reccomend', '0004_auto_20190423_2217'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Ratings',
            new_name='Rating',
        ),
        migrations.AddField(
            model_name='clothingitem',
            name='avg_rating',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
