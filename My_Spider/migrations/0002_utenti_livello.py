# Generated by Django 5.2.1 on 2025-05-27 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('My_Spider', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='utenti',
            name='livello',
            field=models.IntegerField(default=1),
        ),
    ]
