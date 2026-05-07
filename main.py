from models import Giacca, Pantalone, Gilet, Cravatta, Papillon, Pochette
from crud import crea_capo, crea_componente, modifica_capo, elimina_capo, visualizza_tutti
from generatore import genera_dati
from analytics import analizza_tutti, analizza_per_tipo, analizza_per_tipo_e_personalizzazione, analizza_attributi
from export import esporta_csv
from visualizza import grafico_fatturato_per_tipo, grafico_distribuzione_prezzi

# liste condivise tra tutti i moduli, passate come argomento alle funzioni
lista_capi = []
lista_componenti = []

def menu_analisi(): # Sottomenu dedicato alle analisi, richiamato dal menu principale.
    print("\n--- ANALISI ---")
    print("1. Analizza tutti i capi")
    print("2. Analizza solo per tipo di capo")
    print("3. Analizza per tipo e personalizzazione")
    print("4. Analizza attributi (colori, tessuti, taglie)")
    print("0. Torna indietro")
    scelta = input("\nScelta: ").strip()

    if scelta == "1":
        analizza_tutti()
    elif scelta == "2":
        print("\nTipi disponibili: Giacca, Pantalone, Gilet, Cravatta, Papillon, Pochette")
        tipo = input("Inserisci tipo: ").strip()
        analizza_per_tipo(tipo)
    elif scelta == "3":
        print("\nTipi disponibili: Giacca, Pantalone, Gilet, Cravatta, Papillon, Pochette")
        tipo   = input("Inserisci tipo: ").strip()
        valore = input("Inserisci valore personalizzazione: ").strip()
        analizza_per_tipo_e_personalizzazione(lista_capi, lista_componenti, tipo, valore)
    elif scelta == "4":
        analizza_attributi(lista_capi, lista_componenti)
    elif scelta == "0":
        return
    else:
        print("Scelta non valida.")

def menu_visualizzazione(): # Sottomenu dedicato ai grafici, richiamato dal menu principale.
    print("\n--- VISUALIZZAZIONE ---")
    print("1. Grafico fatturato per tipo")
    print("2. Istogramma distribuzione prezzi")
    print("0. Torna indietro")
    scelta = input("\nScelta: ").strip()

    if scelta == "1":
        grafico_fatturato_per_tipo()       # grafico a barre: fatturato per ogni tipo di capo
    elif scelta == "2":
        grafico_distribuzione_prezzi()     # istogramma: distribuzione dei prezzi delle vendite
    elif scelta == "0":
        return
    else:
        print("Scelta non valida.")

def menu():
    genera_dati(lista_capi, lista_componenti)
    print("Dati iniziali generati automaticamente.")

    while True:
        print("\n== SARTORIA ELEGANTE ==")
        print("1. Crea capo")
        print("2. Crea componente")
        print("3. Modifica capo")
        print("4. Elimina capo")
        print("5. Visualizza catalogo")
        print("6. Genera nuovi dati")
        print("7. Analisi")
        print("8. Esporta CSV")
        print("9. Visualizzazione grafici")
        print("0. Esci")
        scelta = input("\nScelta: ").strip()

        if scelta == "1":
            crea_capo(lista_capi)                                # aggiunge un nuovo capo scelto dall'utente
        elif scelta == "2":
            crea_componente(lista_componenti)                    # aggiunge un nuovo componente scelto dall'utente
        elif scelta == "3":
            modifica_capo(lista_capi, lista_componenti)          # modifica un capo esistente tramite codice
        elif scelta == "4":
            elimina_capo(lista_capi, lista_componenti)           # rimuove un capo dalla lista tramite codice
        elif scelta == "5":
            visualizza_tutti(lista_capi, lista_componenti)       # stampa tutto il catalogo
        elif scelta == "6":
            genera_dati(lista_capi, lista_componenti)            # genera e aggiunge nuovi dati casuali
        elif scelta == "7":
            menu_analisi()                                       # entra nel sottomenu analisi
        elif scelta == "8":
            esporta_csv()                                        # scrive le vendite su file vendite.csv
        elif scelta == "9":
            menu_visualizzazione()                               # entra nel sottomenu grafici
        elif scelta == "0":
            print("Arrivederci!")
            break
        else:
            print("Scelta non valida.")

if __name__ == "__main__":
    menu()