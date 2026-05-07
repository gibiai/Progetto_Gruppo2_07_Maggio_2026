# gestisce le operazioni manuali sui capi e sui compomenti di finitura.
# Permette all'utente di creare nuovi oggetti inserendoli
# 
# importiamo tutte le classi da models.py per poter istanziare gli oggetti
from models import Giacca, Pantalone, Gilet, Cravatta, Papillon, Pochette


# funzione di supporto che cerca un elemento nella lista tramite il suo codice univoco
# riceve due parametri: la lista in cui cercare e il codice da trovare
def cerca_per_codice(lista, codice):
    # cicla ogni elemento della lista uno per uno e confronta i codici
    for elemento in lista:
        # confronta il codice dell'elemento con quello cercato
        if elemento.codice == codice:
            # se lo trova lo restituisce subito e si ferma
            return elemento
    # se il ciclo finisce senza trovare nulla restituisce None (valore vuoto)
    return None


# funzione che chiede i dati all'utente e crea un nuovo capo principale
# riceve lista_capi dal main.py: lavora su quella lista, non ne crea una nuova
def crea_capo(lista_capi):
    print("\n--- Crea capo principale ---")
    print("1. Giacca")
    print("2. Pantalone")
    print("3. Gilet")
    # input() restituisce sempre una stringa, .strip() rimuove spazi accidentali
    scelta = input("Tipo: ").strip()

# Seleziona il tipo di oggetto e raccoglie gli attributi universali necessari a ogni capo. In questo caso prima famiglia "CAPI"
# I dati comuni vengono puliti (.strip) per spazi vuoti e convertiti (float) prima di gestire le specifiche.    
    nome    = input("Nome: ").strip()
    tessuto = input("Tessuto: ").strip()
    colore  = input("Colore: ").strip()
    taglia  = input("Taglia: ").strip()
    # float() converte la stringa dell'input in numero decimale per il prezzo
    prezzo  = float(input("Prezzo (€): "))

    # match confronta la scelta con i case: esegue solo il blocco corrispondente
    match scelta:
        case "1":
            # int() converte la stringa in numero intero
            numero_bottoni = int(input("Numero bottoni: "))
            # istanzia Giacca passando tutti gli attributi comuni più quello specifico
            capo = Giacca(codice, nome, tessuto, colore, taglia, prezzo, numero_bottoni)
        case "2":
            tipo_taglio = input("Tipo taglio: ").strip()
            # istanzia Pantalone con il suo attributo specifico
            capo = Pantalone(codice, nome, tessuto, colore, taglia, prezzo, tipo_taglio)
        case "3":
            # confronta la risposta con "s": True se è "s", False in tutti gli altri casi
            revers = input("Revers presente? (s/n): ").strip().lower() == "s"
            # istanzia Gilet con il suo attributo booleano
            capo = Gilet(codice, nome, tessuto, colore, taglia, prezzo, revers)
        case _:
            # case _ è il default: equivale all'else, nessun case corrisponde
            print("Scelta non valida.")
            # return senza valore esce dalla funzione immediatamente senza fare nulla
            return

    # aggiunge l'oggetto appena creato alla lista che arriva dal main.py
    lista_capi.append(capo)
    print(f"\nCapo '{nome}' aggiunto!")


# funzione che chiede i dati all'utente e crea un nuovo componente di finitura
# struttura identica a crea_capo ma per la seconda famiglia di oggetti "COMPONENTI"
def crea_componente(lista_componenti):
    print("\n--- Crea componente di finitura ---")
    print("1. Cravatta")
    print("2. Papillon")
    print("3. Pochette")
    scelta = input("Tipo: ").strip()

    # attributi comuni alla seconda famiglia: c'è materiale al posto di tessuto, manca taglia
    codice    = input("Codice: ").strip()
    nome      = input("Nome: ").strip()
    materiale = input("Materiale: ").strip()
    colore    = input("Colore: ").strip()
    prezzo    = float(input("Prezzo (€): "))

    match scelta:
        case "1":
            # larghezza in centimetri è l'attributo specifico della Cravatta
            larghezza = float(input("Larghezza (cm): "))
            comp = Cravatta(codice, nome, materiale, colore, prezzo, larghezza)
        case "2":
            tipo_chiusura = input("Tipo chiusura: ").strip()
            comp = Papillon(codice, nome, materiale, colore, prezzo, tipo_chiusura)
        case "3":
            piega = input("Piega decorativa: ").strip()
            comp = Pochette(codice, nome, materiale, colore, prezzo, piega)
        case _:
            print("Scelta non valida.")
            return

    # aggiunge il componente alla lista dei componenti che arriva dal main.py
    lista_componenti.append(comp)
    print(f"\nComponente '{nome}' aggiunto!")


# funzione che stampa tutti i capi e i componenti presenti nelle liste
# riceve entrambe le liste perché deve mostrare tutte e due le famiglie
def visualizza_tutti(lista_capi, lista_componenti):
    print("\n--- Capi principali ---")
    # "not lista" è True quando la lista è vuota, quindi non ha elementi
    if not lista_capi:
        print("Nessun capo presente.")
    else:
        for capo in lista_capi:
            # .descrivi() è polimorfico: Python chiama il metodo giusto
            # in base al tipo reale dell'oggetto (Giacca, Pantalone o Gilet)
            # senza che noi dobbiamo sapere quale sia
            capo.descrivi()

    print("\n--- Componenti di finitura ---")
    if not lista_componenti:
        print("Nessun componente presente.")
    else:
        for comp in lista_componenti:
            # stesso meccanismo: .descrivi() funziona su Cravatta, Papillon e Pochette
            comp.descrivi()


# funzione che cerca un elemento tramite codice e permette di modificarne gli attributi
# riceve entrambe le liste perché il codice potrebbe essere in una o nell'altra
def modifica_capo(lista_capi, lista_componenti):
    print("\n--- Modifica capo ---")
    codice = input("Codice del capo da modificare: ").strip()

    # cerca prima tra i capi principali usando la funzione di supporto
    capo = cerca_per_codice(lista_capi, codice)
    # se non lo trova (None) cerca tra i componenti di finitura
    if not capo:
        capo = cerca_per_codice(lista_componenti, codice)
    # se non lo trova neanche lì avvisa l'utente ed esce dalla funzione
    if not capo:
        print("Codice non trovato!")
        return

    # mostra il capo trovato prima di chiedere cosa modificare
    capo.descrivi()
    print("\nCosa vuoi modificare?")
    print("1. Prezzo")
    print("2. Colore")
    print("3. Taglia (solo capi principali)")
    scelta = input("Scelta: ").strip()

    match scelta:
        case "1":
            # modifica direttamente l'attributo sull'oggetto trovato
            capo.prezzo = float(input("Nuovo prezzo (€): "))
            print("Prezzo aggiornato!")
        case "2":
            capo.colore = input("Nuovo colore: ").strip()
            print("Colore aggiornato!")
        case "3":
            # hasattr() controlla se l'oggetto ha quell'attributo senza crashare
            # i componenti non hanno "taglia" quindi senza questo controllo darebbe errore
            if hasattr(capo, "taglia"):
                capo.taglia = input("Nuova taglia: ").strip()
                print("Taglia aggiornata!")
            else:
                print("Questo elemento non ha una taglia!")
        case _:
            print("Scelta non valida.")


# funzione che cerca un elemento tramite codice e lo rimuove dalla lista dopo conferma
def elimina_capo(lista_capi, lista_componenti):
    print("\n--- Elimina capo ---")
    codice = input("Codice del capo da eliminare: ").strip()

    # cerca nei capi e tiene traccia di quale lista usare per la rimozione
    capo  = cerca_per_codice(lista_capi, codice)
    # salviamo il riferimento alla lista: serve a .remove() per sapere da dove togliere
    lista = lista_capi

    # se non è nei capi aggiorna sia l'oggetto trovato che il riferimento alla lista
    if not capo:
        capo  = cerca_per_codice(lista_componenti, codice)
        lista = lista_componenti

    if not capo:
        print("Codice non trovato!")
        return

    # mostra cosa sta per essere eliminato prima di chiedere conferma
    capo.descrivi()
    conferma = input("\nConfermi l'eliminazione? (s/n): ").strip().lower()
    if conferma == "s":
        # .remove() toglie l'oggetto dalla lista giusta (capi o componenti)
        lista.remove(capo)
        print("Eliminato!")
    else:
        print("Eliminazione annullata.")
