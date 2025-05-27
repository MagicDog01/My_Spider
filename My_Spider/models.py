from django.db import models
from django.utils import timezone

class utenti(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    data_creazione = models.DateTimeField(default=timezone.now)
    livello = models.IntegerField(default=1)