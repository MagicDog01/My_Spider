# 🕷 MySpider

**MySpider** è una piattaforma gestionale e social pensata per appassionati di tarantole.
Gli utenti possono registrare i propri esemplari, tenere traccia degli eventi (muta, alimentazione, ecc.), condividere note e foto, interagire con altri utenti, e consultare articoli informativi.

---
## 🧪 Tecnologie utilizzate

### Backend
- **Python** – Linguaggio principale del progetto.
- **Django** – Framework per la gestione della logica, sicurezza e routing lato server.
- **Pillow** – Libreria per la gestione di immagini utente.

### Database
- **SQLite** in locale (facile da configurare) o **PostgreSQL** per ambienti di produzione.

### Frontend
- **HTML/CSS** – Utilizzati per costruire l’interfaccia utente.
- **Bootstrap** – Framework CSS per uno stile responsivo e coerente.
- 
---

## Installazione

### Prerequisiti

* Python 3.10+
* pip
* Git
* Virtualenv (opzionale ma consigliato)
* PostgreSQL o SQLite

### Clonazione del progetto

```bash
git clone https://github.com/TUO-USERNAME/My_Spider.git
cd My_Spider
```

### Creazione ambiente virtuale (opzionale)

```bash
python -m venv venv
source venv/bin/activate        # Su Windows: venv\Scripts\activate
```

### Installazione dipendenze

```bash
pip install -r requirements.txt
```

---

## Avvio del server

### Migrazioni e setup database

```bash
python manage.py migrate
```

### Avvio del server di sviluppo

```bash
python manage.py runserver
```

Il progetto sarà disponibile all’indirizzo:
`http://127.0.0.1:8000/`

---

## Manuale d’uso rapido

### Funzionalità principali:

*    **Registrazione/Login**: convalidata via email.
*    **Gestione tarantole**: aggiungi nome, specie, sesso, data di acquisizione, foto.
*    **Eventi associati**: come muta, alimentazione, accoppiamento, note personali, ecc.
*    **Media e note private**: caricamento di foto e appunti, anche privati (protetti da cifratura).
*    **Articoli/manuali**: accessibili in sola lettura o modificabili da utenti esperti.
*    **Interazione sociale**: commenti, like, segnalazioni, badge per attività.
*    **Filtri e ricerca**: per specie, sesso, eventi, date.
*    **Privacy e sicurezza**: implementazione STRIDE, mitigazioni SQLi, rate limiting, logging e cifratura.

---

##   Credenziali utenti demo

Puoi accedere con uno dei seguenti account demo:

| Ruolo       | Username       | Password   |
| ----------- | -------------- | ---------- |
| Scrittore   | `ok`           | `12345678!`|
| Utente base | `PietroParker` | `12345678!`|
| Utente base | `Mario`        | `12345678!`|


>   *Questi account hanno già alcune tarantole ed eventi registrati per prova.*

---

## 📄 Licenza

Questo progetto è distribuito sotto licenza **MIT**.
Consulta il file [LICENSE](./LICENSE) per maggiori dettagli.

---

