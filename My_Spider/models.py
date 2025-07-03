from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator

class Seguito(models.Model):
    id_seguito = models.AutoField(primary_key=True)
    id_utente_seguace = models.ForeignKey('utenti', on_delete=models.CASCADE, related_name='seguiti', db_column='id_utente_seguace')
    id_utente_seguito = models.ForeignKey('utenti', on_delete=models.CASCADE, related_name='seguaci', db_column='id_utente_seguito')

class utenti(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    data_creazione = models.DateTimeField(default=timezone.now)
    livello = models.IntegerField(default=1, validators=[MinValueValidator(1)])

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

class Articolo(models.Model):
    id_articolo = models.AutoField(primary_key=True)
    titolo = models.CharField(max_length=200)
    testo = models.TextField()
    data = models.DateField()
    id_utente = models.ForeignKey(utenti, on_delete=models.CASCADE, db_column='id_utente')

class Interazione_Articolo(models.Model):
    id_interazione = models.AutoField(primary_key=True)
    id_utente = models.ForeignKey('utenti', on_delete=models.CASCADE, db_column='id_utente')
    id_articolo = models.ForeignKey('Articolo', on_delete=models.CASCADE, db_column='id_articolo')
    tipo = models.CharField(max_length=20)
    testo_commento = models.TextField(blank=True)
    data = models.DateTimeField(default=timezone.now)

class Interazione_Evento(models.Model):
    id_interazione = models.AutoField(primary_key=True)
    id_utente = models.ForeignKey('utenti', on_delete=models.CASCADE, db_column='id_utente')
    id_evento = models.ForeignKey('Evento', on_delete=models.CASCADE, db_column='id_evento')
    tipo = models.CharField(max_length=20)
    testo_commento = models.TextField(blank=True)
    data = models.DateTimeField(default=timezone.now)