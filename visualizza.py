# modulo per la visualizzazione grafica delle vendite
# genera due grafici: fatturato per tipo e distribuzione dei prezzi
import matplotlib.pyplot as plt
from generatore import vendite


# grafico a barre: mostra il fatturato totale per ogni tipo di capo
def grafico_fatturato_per_tipo():

    # controlla che ci siano vendite da mostrare
    if not vendite:
        print("/!\\ Nessun dato disponibile\n(i) Genera prima le vendite.")
        return

    # dizionario che accumula il fatturato per ogni tipo
    fatturati = {}

    # scorre tutte le vendite e somma il fatturato per tipo
    for v in vendite:
        tipo      = v["tipo"]
        fatturato = v["prezzo"] * v["quantita"]

        # se il tipo esiste già lo incrementa, altrimenti lo inizializza
        if tipo in fatturati:
            fatturati[tipo] += fatturato
        else:
            fatturati[tipo] = fatturato

    # separa i tipi (asse x) dai valori (asse y) per passarli a matplotlib
    tipi   = list(fatturati.keys())
    valori = list(fatturati.values())

    # crea il grafico a barre
    plt.figure(figsize=(8, 5))
    plt.bar(tipi, valori, color="steelblue")

    # etichette e titolo
    plt.title("Fatturato per tipo di capo")
    plt.xlabel("Tipo")
    plt.ylabel("Fatturato (€)")

    # ruota le etichette sull'asse x per leggibilità
    plt.xticks(rotation=45)

    # adatta il layout per non tagliare le etichette
    plt.tight_layout()

    plt.show()
    print("Grafico fatturato per tipo generato ✅")


# istogramma: mostra la distribuzione dei prezzi delle vendite
def grafico_distribuzione_prezzi():

    # controlla che ci siano vendite da mostrare
    if not vendite:
        print("/!\\ Nessun dato disponibile\n(i) Genera prima le vendite.")
        return

    # estrae tutti i prezzi dalla lista vendite
    prezzi = []
    for v in vendite:
        prezzi.append(v["prezzo"])

    # crea l'istogramma con 10 intervalli automatici
    plt.figure(figsize=(8, 5))
    plt.hist(prezzi, bins=10, color="coral", edgecolor="black")

    # etichette e titolo
    plt.title("Distribuzione dei prezzi")
    plt.xlabel("Prezzo (€)")
    plt.ylabel("Numero di vendite")

    plt.tight_layout()

    plt.show()
    print("Istogramma prezzi generato ✅")