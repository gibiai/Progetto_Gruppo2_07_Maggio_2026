from models import Giacca, Pantalone, Gilet, Cravatta, Papillon, Pochette


# funzione di supporto che cerca un elemento nella lista tramite il suo codice
def cerca_per_codice(lista, codice):
    for elemento in lista:
        if elemento.codice == codice:
            return elemento
    return None  # se non trova nulla restituisce None


# crea un nuovo capo principale e lo aggiunge alla lista
def crea_capo(lista_capi):
    print("\n--- Crea capo principale ---")
    print("1. Giacca")
    print("2. Pantalone")
    print("3. Gilet")
    scelta = input("Tipo: ").strip()

    # attributi comuni a tutta la prima famiglia
    codice  = input("Codice: ").strip()
    nome    = input("Nome: ").strip()
    tessuto = input("Tessuto: ").strip()
    colore  = input("Colore: ").strip()
    taglia  = input("Taglia: ").strip()
    prezzo  = float(input("Prezzo (€): "))

    # in base alla scelta chiede l'attributo specifico e istanzia la classe giusta
    match scelta:
        case "1":
            numero_bottoni = int(input("Numero bottoni: "))
            capo = Giacca(codice, nome, tessuto, colore, taglia, prezzo, numero_bottoni)
        case "2":
            tipo_taglio = input("Tipo taglio: ").strip()
            capo = Pantalone(codice, nome, tessuto, colore, taglia, prezzo, tipo_taglio)
        case "3":
            revers = input("Revers presente? (s/n): ").strip().lower() == "s"
            capo = Gilet(codice, nome, tessuto, colore, taglia, prezzo, revers)
        case _:
            print("Scelta non valida.")
            return

    lista_capi.append(capo)
    print(f"\nCapo '{nome}' aggiunto ✅")


# crea un nuovo componente di finitura e lo aggiunge alla lista
def crea_componente(lista_componenti):
    print("\n--- Crea componente di finitura ---")
    print("1. Cravatta")
    print("2. Papillon")
    print("3. Pochette")
    scelta = input("Tipo: ").strip()

    # attributi comuni a tutta la seconda famiglia
    codice    = input("Codice: ").strip()
    nome      = input("Nome: ").strip()
    materiale = input("Materiale: ").strip()
    colore    = input("Colore: ").strip()
    prezzo    = float(input("Prezzo (€): "))

    # in base alla scelta chiede l'attributo specifico e istanzia la classe giusta
    match scelta:
        case "1":
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

    lista_componenti.append(comp)
    print(f"\nComponente '{nome}' aggiunto ✅")


# stampa tutti i capi e i componenti presenti nelle liste
def visualizza_tutti(lista_capi, lista_componenti):
    print("\n--- Capi principali ---")
    if not lista_capi:
        print("Nessun capo presente.")
    else:
        for capo in lista_capi:
            capo.descrivi()  # metodo polimorfico: ogni classe lo gestisce a modo suo

    print("\n--- Componenti di finitura ---")
    if not lista_componenti:
        print("Nessun componente presente.")
    else:
        for comp in lista_componenti:
            comp.descrivi()


# cerca un capo o componente tramite codice e permette di modificarne alcuni attributi
def modifica_capo(lista_capi, lista_componenti):
    print("\n--- Modifica capo ---")
    codice = input("Codice del capo da modificare: ").strip()

    # cerca prima tra i capi principali, poi tra i componenti
    capo = cerca_per_codice(lista_capi, codice)
    if not capo:
        capo = cerca_per_codice(lista_componenti, codice)
    if not capo:
        print("Codice non trovato ⚠️")
        return

    capo.descrivi()
    print("\nCosa vuoi modificare?")
    print("1. Prezzo")
    print("2. Colore")
    print("3. Taglia (solo capi principali)")
    scelta = input("Scelta: ").strip()

    match scelta:
        case "1":
            capo.prezzo = float(input("Nuovo prezzo (€): "))
            print("Prezzo aggiornato ✅")
        case "2":
            capo.colore = input("Nuovo colore: ").strip()
            print("Colore aggiornato ✅")
        case "3":
            # hasattr controlla se l'oggetto ha quell'attributo, evita errori sui componenti
            if hasattr(capo, "taglia"):
                capo.taglia = input("Nuova taglia: ").strip()
                print("Taglia aggiornata ✅")
            else:
                print("Questo elemento non ha una taglia ⚠️")
        case _:
            print("Scelta non valida.")


# cerca un capo o componente tramite codice e lo rimuove dalla lista dopo conferma
def elimina_capo(lista_capi, lista_componenti):
    print("\n--- Elimina capo ---")
    codice = input("Codice del capo da eliminare: ").strip()

    # cerca prima tra i capi, tiene traccia di quale lista usare per la rimozione
    capo  = cerca_per_codice(lista_capi, codice)
    lista = lista_capi

    # se non è nei capi lo cerca tra i componenti e aggiorna il riferimento alla lista
    if not capo:
        capo  = cerca_per_codice(lista_componenti, codice)
        lista = lista_componenti

    if not capo:
        print("Codice non trovato ⚠️")
        return

    capo.descrivi()
    conferma = input("\nConfermi l'eliminazione? (s/n): ").strip().lower()
    if conferma == "s":
        lista.remove(capo)
        print("Eliminato ✅")
    else:
        print("Eliminazione annullata.")