<img width="272" height="78" alt="logo" src="https://github.com/user-attachments/assets/54fc9ee5-45dc-4c8a-b977-6f6a3253ca17" />

**MySpider** è una piattaforma gestionale e social pensata per appassionati di tarantole.
Gli utenti possono registrare i propri esemplari, tenere traccia degli eventi (muta, alimentazione, ecc.), condividere note e foto, interagire con altri utenti, e consultare articoli informativi.

---
##  Tecnologie utilizzate

### Backend
- **Python** – Linguaggio principale del progetto.
- **Django** – Framework per la gestione della logica, sicurezza e routing lato server.
- **Pillow** – Libreria per la gestione di immagini utente.

### Database
- **SQLite** in locale (facile da configurare) 

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
git clone https://github.com/MagicDog01/My_Spider.git
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
*    <img width="952" height="434" alt="login" src="https://github.com/user-attachments/assets/837acdce-ce6e-41da-af26-b31bd51d7baa" />

*    **Gestione tarantole**: aggiungi nome, specie, sesso, data di acquisizione, foto.
*    **Eventi associati**: come muta, alimentazione, accoppiamento, note personali, ecc.
*    **Media e note private**: caricamento di foto e appunti, anche privati (protetti da cifratura).
*    <img width="943" height="434" alt="screen diario" src="https://github.com/user-attachments/assets/1d7433b6-b4ec-48e3-9f4f-a7fa8e713713" />
*    **Articoli/manuali**: accessibili in sola lettura o modificabili da utenti esperti.
*    <img width="943" height="428" alt="biblioteca" src="https://github.com/user-attachments/assets/483860f1-d99b-4225-bc1d-bc37c06bba65" />

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


>   *Questi account hanno già alcune tarantole, eventi e articoli registrati per prova.*

---

## 📄 Licenza

Questo progetto è distribuito sotto licenza **MIT**.
Consulta il file [LICENSE](./LICENSE) per maggiori dettagli.

---

