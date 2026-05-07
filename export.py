# --- modulo export.py ---

import csv
import os
from generatore import vendite

# Scrive vendite[] su file CSV. Calcola fatturato al momento dell'export.
percorso = os.getcwd()
def esporta_csv(filepath = percorso + "/vendite.csv"):

    if not vendite:
        print("/!\\ Nessun dato da esportare\n(i) Genera prima le vendite.\n")
        return
    
    # Colonne del CSV
    colonne = ["codice",
                "nome",
                "tipo",
                "famiglia",
                "prezzo",
                "quantita",
                "fatturato"]
    
    with open(filepath, mode = "w", newline="", encoding="utf-8") as f:
        # classe della libreria standard che scrive dizionari Python come righe in un file CSV.
        writer = csv.DictWriter(f, fieldnames = colonne)
        # scrive la prima riga del CSV con i nomi delle colonne
        writer.writeheader()
        
        # scrive i valori nel CSV riga per riga
        for v in vendite:
            writer.writerow({
                "codice":    v["codice"],
                "nome":      v["nome"],
                "tipo":      v["tipo"],
                "famiglia":  v["famiglia"],
                "prezzo":    v["prezzo"],
                "quantita":  v["quantita"],
                 # calcolato durante l'export poichè è un valore derivato
                 # e se il prezzo fosse stato modificato via CRUD il dato 
                 # pre-calcolato sarebbe inconsistente.
                "fatturato": round(v["prezzo"] * v["quantita"], 2)
            })
    
    # Print di conferma
    print(f"--- ✔ Esportato  ---\nPath: {filepath}\nRighe: ({len(vendite)})")
