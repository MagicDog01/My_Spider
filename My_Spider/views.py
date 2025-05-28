from django.shortcuts import render, redirect
from My_Spider.models import utenti
from django.contrib.auth.hashers import (make_password, check_password)
import re

def login_view(request):
        if request.method == "POST":
            username = request.POST["username"]
            password = request.POST["password"]
            try:
                user = utenti.objects.get(username=username)
                if check_password(password, user.password):
                    request.session['logged_in'] = True
                    request.session['username'] = username  # Salva il nome utente nella sessione
                    return redirect("account")
                return render(request, "login.html", {"error": "Password non corretta"})
            except utenti.DoesNotExist:
                return render(request, "login.html", {"error": "Username non trovato"})
        return render(request, "login.html")

def is_valid_password(password):
    # Almeno 8 caratteri, almeno un numero e un carattere speciale
    if len(password) < 8:
        return False
    if not re.search(r"\d", password):
        return False
    if not re.search(r"[^\w\s]", password):
        return False
    return True

def signup_view(request):
        if request.method == "POST":
            username = request.POST["username"]
            email = request.POST["email"]
            password = request.POST["password"]

            if not is_valid_password(password):
                return render(request, "signup.html",
                   {"error": "La password deve avere almeno 8 caratteri, un numero e un carattere speciale."})

            if utenti.objects.filter(username=username).exists():
                return render(request, "signup.html", {"error": "Username già esistente"})

            if utenti.objects.filter(email=email).exists():
                return render(request, "signup.html", {"error": "Email già registrata"})

            user = utenti(username=username, email=email, password=make_password(password))
            user.save()

            # Imposta la sessione dopo la registrazione
            request.session['logged_in'] = True
            request.session['username'] = username

            return redirect("account")
        return render(request, "signup.html")

def home_view(request):
    return render(request, "home.html")

def account_view(request):
        if request.session.get('logged_in'):
            context = {
                'username': request.session.get('username', 'Utente')  # Prende il nome utente dalla sessione
            }
            return render(request, 'account.html', context)
        return redirect('login')


def logout_view(request):
    request.session.flush()  # Pulisce tutti i dati della sessione
    request.session.modified = True  # Assicura che le modifiche vengano salvate
    return redirect('login')

