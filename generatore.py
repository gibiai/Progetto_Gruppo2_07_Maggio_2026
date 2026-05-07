# simula vendite a livello casuale, se gia inserito da utente capi manualmente li usa come base
# altrimenti pesca randomico dalle liste predefinite
# ogni vendita viene salvata come dizionario nella lista globale vendite[] che export.py poi salverà nel csv
import random
from models import Giacca, Pantalone, Gilet, Cravatta, Papillon, Pochette

# BANCHE DATI
# liste di valori casuali realistici da cui pescheremo con random.choice
tessuti   = ["Lana", "Cashmere", "Cotone", "Seta", "Flanella", "Tweed"]
colori    = ["Nero", "Grigio antracite", "Blu navy", "Bordeaux", "Beige", "Grigio chiaro"]
taglie    = ["44", "46", "48", "50", "52", "54"]
materiali = ["Seta", "Cotone", "Poliestere", "Lino"]
tagli     = ["Classico", "Slim", "Regular", "Sartoriale"]
chiusure  = ["Regolabile", "A clip", "A nodo fisso"]
pieghe    = ["A punta", "A tasca", "A ventaglio", "Piatta"]
nomi_capo = ["Elegante", "Oxford", "Milano", "Venezia", "Torino", "Roma", "Napoli"]
nomi_comp = ["Classica", "Luxury", "Slim", "Premium", "Essential"]

# lista globale delle vendite: ogni vendita è un dizionario con i campi attesi da export.py
vendite = []


# genera n vendite casuali partendo dai capi già inseriti manualmente
# se le liste sono vuote crea oggetti casuali al volo
def genera_dati(lista_capi, lista_componenti, n=10):

    # se non ci sono dati manuali genera oggetti casuali da zero
    # divisione intera // genera metà esatta evitando numeri decimali
    # extend() aggiunge gli elementi direttamente alle liste originali che arrivano dal main
    # essendo le liste oggetti mutabili riflettono immediatamente su tutto il programma senza usare return
    # serve a evitare di sovrascrivere o aggiungere dati inutili se l'utente ha già inserito qualcosa manualmente
    # è una protezione per l'integrità dei dati
    if not lista_capi and not lista_componenti:
        lista_capi.extend(_genera_capi_casuali(n // 2))
        lista_componenti.extend(_genera_componenti_casuali(n // 2))

    # unisce le due liste per poter pescare da entrambe le famiglie
    tutti = lista_capi + lista_componenti

    for i in range(n):
        oggetto  = random.choice(tutti)  # sceglie un capo o componente a caso
        quantita = random.randint(1, 10)

        # determina la famiglia in base a quale lista contiene l'oggetto
        if oggetto in lista_capi:
            famiglia = "Capo principale"
        else:
            famiglia = "Componente finitura"

        # crea il dizionario con i campi che export.py si aspetta
        vendita = {
            "codice":   oggetto.codice,
            "nome":     oggetto.nome,
            "tipo":     oggetto.get_tipo(),  # metodo polimorfico: ogni classe lo gestisce
            "famiglia": famiglia,
            "prezzo":   oggetto.prezzo,
            "quantita": quantita,
        }
        vendite.append(vendita)

    print(f"\n{n} vendite generate ✅")

    # riepilogo rapido del totale in memoria
    # Generator Expression calcola i numeri uno alla volta e li "passa" subito a sum()
    fatturato_totale = sum(v["prezzo"] * v["quantita"] for v in vendite)
    print(f"Totale vendite in memoria: {len(vendite)}")
    print(f"Fatturato totale stimato:  €{fatturato_totale:.2f}\n")


# crea n capi principali casuali senza chiedere input all'utente
def _genera_capi_casuali(n):
    capi = []
    for i in range(n):
        # sceglie casualmente quale tipo di capo creare
        tipo = random.choice(["giacca", "pantalone", "gilet"])  # "pesca" a caso dentro le banche dati

        if tipo == "giacca":
            capo = Giacca(
                codice         = f"G{i:03d}",
                nome           = f"Giacca {random.choice(nomi_capo)}",
                tessuto        = random.choice(tessuti),
                colore         = random.choice(colori),
                taglia         = random.choice(taglie),
                prezzo         = round(random.uniform(200, 900), 2),
                numero_bottoni = random.randint(1, 3)
            )
        elif tipo == "pantalone":
            capo = Pantalone(
                codice      = f"P{i:03d}",
                nome        = f"Pantalone {random.choice(nomi_capo)}",
                tessuto     = random.choice(tessuti),
                colore      = random.choice(colori),
                taglia      = random.choice(taglie),
                prezzo      = round(random.uniform(100, 500), 2),
                tipo_taglio = random.choice(tagli)
            )
        else:
            capo = Gilet(
                codice          = f"GI{i:03d}",
                nome            = f"Gilet {random.choice(nomi_capo)}",
                tessuto         = random.choice(tessuti),
                colore          = random.choice(colori),
                taglia          = random.choice(taglie),
                prezzo          = round(random.uniform(80, 350), 2),
                revers_presente = random.choice([True, False])
            )
        capi.append(capo)
    return capi


# crea n componenti di finitura casuali senza chiedere input all'utente
def _genera_componenti_casuali(n):
    componenti = []
    for i in range(n):
        # sceglie casualmente quale tipo di componente creare
        tipo = random.choice(["cravatta", "papillon", "pochette"])

        if tipo == "cravatta":
            comp = Cravatta(
                codice    = f"CR{i:03d}",
                nome      = f"Cravatta {random.choice(nomi_comp)}",
                materiale = random.choice(materiali),
                colore    = random.choice(colori),
                prezzo    = round(random.uniform(30, 200), 2),
                larghezza = round(random.uniform(6.0, 9.5), 1)
            )
        elif tipo == "papillon":
            comp = Papillon(
                codice        = f"PA{i:03d}",
                nome          = f"Papillon {random.choice(nomi_comp)}",
                materiale     = random.choice(materiali),
                colore        = random.choice(colori),
                prezzo        = round(random.uniform(25, 150), 2),
                tipo_chiusura = random.choice(chiusure)
            )
        else:
            comp = Pochette(
                codice           = f"PO{i:03d}",
                nome             = f"Pochette {random.choice(nomi_comp)}",
                materiale        = random.choice(materiali),
                colore           = random.choice(colori),
                prezzo           = round(random.uniform(20, 120), 2),
                piega_decorativa = random.choice(pieghe)
            )
        componenti.append(comp)
    return componenti
