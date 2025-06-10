from django.shortcuts import render, redirect
from My_Spider.models import utenti, spider
from django.contrib.auth.hashers import make_password, check_password
from django.views.decorators.csrf import csrf_exempt
import re

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        try:
            user = utenti.objects.get(username=username)
            if check_password(password, user.password):
                request.session['logged_in'] = True
                request.session['username'] = username
                return redirect("account")
            return render(request, "login.html", {"error": "Password non corretta"})
        except utenti.DoesNotExist:
            return render(request, "login.html", {"error": "Username non trovato"})
    return render(request, "login.html")

def is_valid_password(password):
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

        request.session['logged_in'] = True
        request.session['username'] = username
        return redirect("account")
    return render(request, "signup.html")

def home_view(request):
    return render(request, "home.html")

def diario_view(request):
    if request.session.get('logged_in'):
        user = utenti.objects.get(username=request.session['username'])
        spiders = spider.objects.filter(utente=user).order_by('-id')
        context = {
            'username': request.session.get('username', 'Utente'),
            'spiders': spiders
        }
        return render(request, 'diario.html', context)
    return redirect('login')

def cerca_view(request):
    if request.session.get('logged_in'):
        context = {
            'username': request.session.get('username', 'Utente')
        }
        return render(request, 'cerca.html', context)
    return redirect('login')

def biblioteca_view(request):
    if request.session.get('logged_in'):
        context = {
            'username': request.session.get('username', 'Utente')
        }
        return render(request, 'biblioteca.html', context)
    return redirect('login')

def account_view(request):
    if request.session.get('logged_in'):
        context = {
            'username': request.session.get('username', 'Utente')
        }
        return render(request, 'account.html', context)
    return redirect('login')

def logout_view(request):
    request.session.flush()
    request.session.modified = True
    return redirect('login')

def add_spider(request):
    if not request.session.get('logged_in'):
        return redirect('login')
    user = utenti.objects.get(username=request.session['username'])
    if request.method == "POST":
        nome = request.POST.get('nome')
        eta = request.POST.get('eta')
        unita_eta = request.POST.get('unita_eta')
        sesso = request.POST.get('sesso')
        specie = request.POST.get('specie')
        icona = request.POST.get('icona')
        nuovo_spider = spider(
            nome=nome,
            eta=int(eta),
            unita_eta=unita_eta,
            sesso=sesso,
            specie=specie,
            utente=user,
            icona=icona
        )
        nuovo_spider.save()
        return redirect('diario')
    # Aggiungi un return anche per GET o altri metodi
    return redirect('diario')

@csrf_exempt
def delete_spider(request, spider_id):
    if request.method == "POST" and request.session.get('logged_in'):
        user = utenti.objects.get(username=request.session['username'])
        try:
            s = spider.objects.get(id=spider_id, utente=user)
            s.delete()
        except spider.DoesNotExist:
            pass
    return redirect('diario')