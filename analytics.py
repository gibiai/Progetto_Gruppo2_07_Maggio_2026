# --- modulo analytics.py ---
from generatore import vendite

# mappa get_tipo() → nome attributo di personalizzazione
ATTRIBUTI_PERSONALIZZAZIONE = {

    "Giacca":    "numero_bottoni",
    "Pantalone": "tipo_taglio",
    "Gilet":     "revers_presente",

    "Cravatta":  "larghezza",
    "Papillon":  "tipo_chiusura",
    "Pochette":  "piega_decorativa",
}

# calcola statistiche di vendita e fatturato per ogni elemento della lista vendite
def analizza_tutti():

    # controllo: se non ci sono vendite evita errori
    if not vendite:
        print("/!\\ Nessun dato disponibile")
        print("(i) Usa prima 'Genera dati'")
        return

    print("\n--- ANALISI COMPLETA ---\n")

    totale = 0

    # scorre tutte le vendite presenti in memoria
    for v in vendite:
        # calcolo fatturato singola vendita
        fatturato = v["prezzo"] * v["quantita"]

        # aggiornamento totale generale
        totale += fatturato
        
        # stampa dettagli vendita
        print(
            f"Tipo: {v['tipo']}\n"
            f"Nome: {v['nome']}\n"
            f"Quantità: {v['quantita']}\n"
            f"Fatturato: {fatturato:.2f} €\n"
        )

    print("-" * 35)
    print(f"FATTURATO TOTALE: {totale:.2f} €\n")


# calcola statistiche di vendita e fatturato filtrando per nome classe (tipo)
def analizza_per_tipo(tipo_richiesto):

    # filtro delle vendite tramite list comprehension
    risultati = [

        v for v in vendite
        if v["tipo"].lower() == tipo_richiesto.lower()
    ]

    # controllo risultati
    if not risultati:
        print(f"/!\\ Nessun dato per '{tipo_richiesto}'.")
        return

    print(f"\n--- ANALISI: {tipo_richiesto.upper()} ---\n")

    totale = 0

    for v in risultati:

        fatturato = v["prezzo"] * v["quantita"]
        totale += fatturato

        print(
            f"Nome: {v['nome']}\n"
            f"Quantità: {v['quantita']}\n"
            f"Fatturato: {fatturato:.2f} €\n"
        )

    print("-" * 35)
    print(f"FATTURATO TOTALE: {totale:.2f} €\n")

def analizza_per_tipo_e_personalizzazione(
    lista_capi,
    lista_componenti,
    tipo,
    valore
):

    # controllo presenza vendite
    if not vendite:
        print("/!\\ Nessun dato disponibile")
        print("(i) Usa prima 'Genera dati'")
        return

    # unisce le due famiglie in una lista unica
    tutti = lista_capi + lista_componenti

    trovati = []

    # STEP 1: filtro degli oggetti reali tramite tipo & attributo personalizzato
    for obj in tutti:

        # confronto sul tipo dell'oggetto
        if obj.get_tipo().lower() == tipo.lower():

            # recupera il nome dell'attributo personalizzato
            attr = ATTRIBUTI_PERSONALIZZAZIONE.get(obj.get_tipo())

            # sicurezza: controlla che esista
            if attr:

                # recupera dinamicamente il valore dell'attributo
                valore_attributo = str(
                    getattr(obj, attr)
                ).lower()

                # verifica se il valore cercato è contenuto
                if str(valore).lower() in valore_attributo:

                    trovati.append(obj)

    # STEP 2: estrae i codici degli oggetti trovati

    codici_trovati = {
        obj.codice
        for obj in trovati
    }

    # STEP 3: filtra le vendite usando i codici trovati

    risultati = [
        v for v in vendite
        if v["codice"] in codici_trovati
    ]

    # controllo risultati
    if not risultati:
        print("Nessun risultato trovato.")
        return

    print(
        f"\n===== ANALISI FILTRATA "
        f"{tipo.upper()} / {valore} =====\n"
    )

    totale = 0
    for v in risultati:

        fatturato = v["prezzo"] * v["quantita"]
        totale += fatturato

        print(
            f"Nome: {v['nome']} "
            f"Quantità: {v['quantita']}   "
            f"Fatturato: {fatturato:.2f} €"
        )

    print("-" * 40)
    print(f"Fatturato filtrato: {totale:.2f} €\n")

def analizza_attributi(lista_capi, lista_componenti):

    # ANALISI COLORI
    colori = {}
    # scorre tutti gli oggetti
    for obj in lista_capi + lista_componenti:
        # se il colore esiste già incrementa il contatore
        if obj.colore in colori:
            colori[obj.colore] += 1
        # altrimenti inizializza a 1
        else:
            colori[obj.colore] = 1
    print("\n--- COLORI PIÙ FREQUENTI ---")
    # ordinamento decrescente per frequenza
    for colore, n in sorted(
        colori.items(),
        key=lambda x: x[1],
        reverse=True
    ):
        print(f"{colore}: {n} articoli")


    # ANALISI TESSUTI
    tessuti = {}
    # solo i capi principali possiedono "tessuto"
    for obj in lista_capi:
        if obj.tessuto in tessuti:
            tessuti[obj.tessuto] += 1
        else:
            tessuti[obj.tessuto] = 1
    print("\n--- TESSUTI PIÙ USATI ---")
    for tessuto, n in sorted(
        tessuti.items(),
        key=lambda x: x[1],
        reverse=True
    ):
        print(f"{tessuto}: {n} articoli")

    # ANALISI TAGLIE PANTALONI
    taglie = {}
    for obj in lista_capi:
        # filtra solo i pantaloni
        if obj.get_tipo() == "Pantalone":
            t = obj.taglia
            if t in taglie:
                taglie[t] += 1
            else:
                taglie[t] = 1

    # stampa solo se esistono pantaloni
    if taglie:
        print("\n--- TAGLIE PANTALONI ---")
        for taglia, n in sorted(
            taglie.items(),
            key=lambda x: x[1],
            reverse=True
        ):
            print(f"{taglia:<10} {n} articoli")

    print()