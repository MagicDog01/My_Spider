from django.shortcuts import render, redirect, get_object_or_404
from My_Spider.models import utenti, spider, Evento, Articolo
from django.contrib.auth.hashers import make_password, check_password
from django.views.decorators.csrf import csrf_exempt
from .forms import EventoForm, ArticoloForm
from django.utils import timezone
import re
import time
def login_view(request):
    max_attempts = 3
    block_minutes = 15
    blocked_until = request.session.get('blocked_until')
    if blocked_until and time.time() < blocked_until:
        minuti_restanti = int((blocked_until - time.time()) // 60) + 1
        return render(request, "login.html", {"error": f"Troppi tentativi falliti. Riprova tra {minuti_restanti} minuti."})

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        # Inizializza tentativi se non presenti
        attempts = request.session.get('login_attempts', 0)

        try:
            user = utenti.objects.get(username=username)
            if check_password(password, user.password):
                request.session['logged_in'] = True
                request.session['username'] = username
                request.session['login_attempts'] = 0  # reset tentativi
                return redirect("account")
            else:
                attempts += 1
        except utenti.DoesNotExist:
            attempts += 1

        request.session['login_attempts'] = attempts

        if attempts >= max_attempts:
            request.session['blocked_until'] = time.time() + block_minutes * 60
            return render(request, "login.html", {"error": f"Troppi tentativi falliti. Riprova tra {block_minutes} minuti."})
        else:
            return render(request, "login.html", {"error": f"Credenziali errate. Tentativi rimasti: {max_attempts - attempts}"})

    # Reset tentativi se si accede alla pagina senza POST
    request.session['login_attempts'] = 0
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
    context = {
        'logged_in': request.session.get('logged_in', False),
        'username': request.session.get('username', 'Utente')
    }
    return render(request, "home.html", context)

def diario_view(request):
    logged_in = request.session.get('logged_in', False)
    if logged_in:
        user = utenti.objects.get(username=request.session['username'])
        spiders = spider.objects.filter(utente=user).order_by('-id')
        context = {
            'logged_in': logged_in,
            'username': request.session.get('username', 'Utente'),
            'spiders': spiders
        }
        return render(request, 'diario.html', context)
    return redirect('login')

def cerca_view(request):
    logged_in = request.session.get('logged_in', False)
    if logged_in:
        context = {
            'logged_in': logged_in,
            'username': request.session.get('username', 'Utente')
        }
        return render(request, 'cerca.html', context)
    return redirect('login')

def biblioteca_view(request):
    logged_in = request.session.get('logged_in', False)
    if logged_in:
        user = utenti.objects.get(username=request.session['username'])
        articoli = Articolo.objects.all().order_by('-data')
        mostra_pulsante = user.livello >= 10
        context = {
            'logged_in': logged_in,
            'username': user.username,
            'articoli': articoli,
            'mostra_pulsante': mostra_pulsante
        }
        return render(request, 'biblioteca.html', context)
    return redirect('login')

def account_view(request):
    logged_in = request.session.get('logged_in', False)
    context = {
        'logged_in': logged_in,
        'username': request.session.get('username', 'Utente')
    }
    if logged_in:
        return render(request, 'account.html', context)
    return redirect('login')

def logout_view(request):
    request.session.flush()
    request.session.modified = True
    return redirect('login')

def add_spider(request):
    logged_in = request.session.get('logged_in', False)
    if not logged_in:
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
        # Incrementa il livello dell'utente
        user.livello += 1
        user.save()
        return redirect('diario')
    return redirect('diario')

@csrf_exempt
def delete_spider(request, spider_id):
    logged_in = request.session.get('logged_in', False)
    if request.method == "POST" and logged_in:
        user = utenti.objects.get(username=request.session['username'])
        try:
            s = spider.objects.get(id=spider_id, utente=user)
            s.delete()
        except spider.DoesNotExist:
            pass
    return redirect('diario')

def crea_evento_view(request, spider_id):
    logged_in = request.session.get('logged_in', False)
    if not logged_in:
        return redirect('login')
    tarantola = get_object_or_404(spider, id=spider_id)
    if request.method == 'POST':
        form = EventoForm(request.POST, request.FILES)
        if form.is_valid():
            evento = form.save(commit=False)
            evento.data = timezone.now()
            evento.id_tarantola = tarantola
            evento.save()
            # Incrementa il livello dell'utente
            user = utenti.objects.get(username=request.session['username'])
            user.livello += 1
            user.save()
            return redirect('diario')
    else:
        form = EventoForm()
    context = {
        'logged_in': logged_in,
        'username': request.session.get('username', 'Utente'),
        'form': form,
        'tarantola': tarantola
    }
    return render(request, 'crea_evento.html', context)

def lista_eventi_view(request, spider_id):
    logged_in = request.session.get('logged_in', False)
    if not logged_in:
        return redirect('login')
    eventi = Evento.objects.filter(id_tarantola=spider_id)
    context = {
        'logged_in': logged_in,
        'username': request.session.get('username', 'Utente'),
        'eventi': eventi
    }
    return render(request, 'lista_eventi.html', context)

def elimina_evento(request, pk):
    logged_in = request.session.get('logged_in', False)
    if not logged_in:
        return redirect('login')
    evento = get_object_or_404(Evento, pk=pk)
    spider_id = evento.id_tarantola.id
    evento.delete()
    return redirect('lista_eventi', spider_id=spider_id)

def crea_articolo(request):
    logged_in = request.session.get('logged_in', False)
    if not logged_in:
        return redirect('login')
    if request.method == 'POST':
        form = ArticoloForm(request.POST, request.FILES)
        if form.is_valid():
            articolo = form.save(commit=False)
            user = utenti.objects.get(username=request.session['username'])
            articolo.id_utente = user
            articolo.data = timezone.now()
            articolo.save()
            return redirect('biblioteca')
    else:
        form = ArticoloForm()
    context = {
        'logged_in': logged_in,
        'username': request.session.get('username', 'Utente'),
        'form': form
    }
    return render(request, 'crea_articolo.html', context)

def visualizzazione_articolo(request, pk):
    logged_in = request.session.get('logged_in', False)
    if not logged_in:
        return redirect('login')
    articolo = get_object_or_404(Articolo, pk=pk)
    context = {
        'logged_in': logged_in,
        'username': request.session.get('username', 'Utente'),
        'articolo': articolo
    }
    return render(request, 'visualizzazione_articolo.html', context)

def elimina_articolo(request, pk):
    if request.method == "POST":
        articolo = get_object_or_404(Articolo, pk=pk)
        if request.session.get('logged_in') and request.session.get('username') == articolo.id_utente.username:
            articolo.delete()
    return redirect('biblioteca')