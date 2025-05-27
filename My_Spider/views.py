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
                request.session['user_id'] = user.id
                return redirect("account")
            else:
                return render(request, "login.html", {"error": "Credenziali non valide"})
        except utenti.DoesNotExist:
            return render(request, "login.html", {"error": "Credenziali non valide"})
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
        user = utenti(username=username, email=email, password=make_password(password))
        user.save()
        return redirect("account")
    return render(request, "signup.html")

def home_view(request):
    return render(request, "home.html")
def account_view(request):
    user_id = request.session.get('user_id')
    username = None
    if user_id:
        try:
            user = utenti.objects.get(id=user_id)
            username = user.username
        except utenti.DoesNotExist:
            pass
    return render(request, "account.html", {"username": username})