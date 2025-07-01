from django.db import models
from django.utils import timezone

class utenti(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    data_creazione = models.DateTimeField(default=timezone.now)
    livello = models.IntegerField(default=1)

class spider(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    eta = models.IntegerField()
    sesso = models.CharField(max_length=10)
    specie = models.CharField(max_length=50)
    utente = models.ForeignKey(utenti, on_delete=models.CASCADE)
    icona = models.CharField(max_length=100)
    unita_eta = models.CharField(max_length=10, default='anni')

class Evento(models.Model):
    id_evento = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=50)
    data = models.DateField()
    note = models.TextField(blank=True)
    foto = models.ImageField(upload_to='eventi_foto/', blank=True, null=True)
    id_tarantola = models.ForeignKey(spider, on_delete=models.CASCADE, related_name='eventi')