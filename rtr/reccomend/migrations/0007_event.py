# Generated by Django 2.1.5 on 2019-04-29 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reccomend', '0006_clothingitem_img_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=50)),
                ('img_url', models.CharField(max_length=200)),
            ],
        ),
    ]
