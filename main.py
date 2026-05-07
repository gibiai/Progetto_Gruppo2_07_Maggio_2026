from models import *
from crud import crea_capo, modifica_capo, elimina_capo
from generatore import genera_dati
from analytics import analizza_tutti, analizza_per_tipo, analizza_per_tipo_e_personalizzazione
from export import esporta_csv

# liste condivise tra tutti i moduli, passate come argomento alle funzioni
lista_capi = []
lista_componenti = []

def menu_analisi():
    print("\n--- ANALISI ---")
    print("1. Analizza tutti i capi")
    print("2. Analizza solo per tipo di capo")
    print("3. Analizza per tipo e personalizzazione")
    print("0. Torna indietro")

    scelta = input("\nScelta: ").strip()

    if scelta == "1":
        analizza_tutti(lista_capi)
    elif scelta == "2":
        analizza_per_tipo(lista_capi)
    elif scelta == "3":
        analizza_per_tipo_e_personalizzazione(lista_capi)
    elif scelta == "0":
        return
    else:
        print("Scelta non valida.")

def menu():
    genera_dati(lista_capi, lista_componenti)
    print("Dati iniziali generati automaticamente.")

    while True:
        print("\n== SARTORIA ELEGANTE ==") # menu sartoria in cui si può creare un capo, analizzarlo ed esportarlo
        print("1. Crea capo")
        print("2. Modifica capo")
        print("3. Elimina capo")
        print("4. Genera nuovi dati")
        print("5. Analisi")
        print("6. Esporta CSV")
        print("0. Esci")

        scelta = input("\nScelta: ").strip()

        if scelta == "1":
            crea_capo(lista_capi, lista_componenti)  # aggiunge un nuovo capo scelto dall'utente
        elif scelta == "2":
            modifica_capo(lista_capi, lista_componenti)  # modifica un capo esistente tramite codice
        elif scelta == "3":
            elimina_capo(lista_capi, lista_componenti)  # rimuove un capo dalla lista tramite codice
        elif scelta == "4":
            genera_dati(lista_capi, lista_componenti) # genera e aggiunge nuovi dati casuali
        elif scelta == "5":
            menu_analisi()  # entra nel sottomenu analisi
        elif scelta == "6":
            esporta_csv(lista_capi, lista_componenti) # scrive le liste su file vendite.csv
        elif scelta == "0":
            print("Arrivederci!")
            break
        else:
            print("Scelta non valida.")

if __name__ == "__main__":
    menu()
