Sartoria Elegante 🧵

Sistema di gestione per una sartoria che realizza suite eleganti, smoking e completi classici.
Progetto di gruppo — Corso Python Formatemp 2026.

---

## Descrizione

Programma Python a riga di comando che permette di gestire due famiglie di oggetti:
- **Capi principali** — Giacca, Pantalone, Gilet
- **Componenti di finitura** — Cravatta, Papillon, Pochette

Il sistema consente di creare, modificare ed eliminare capi, generare vendite in modo casuale e analizzare i dati del magazzino.

---

## Funzionalità

- Creazione manuale di capi principali e componenti di finitura
- Modifica ed eliminazione di capi esistenti
- Generazione automatica di dati di vendita casuali
- Analisi dei capi (tutti, per tipo, per tipo e personalizzazione)
- Esportazione dei dati in formato CSV

---

## Struttura del progetto

```
sartoria/
│
├── main.py              # menu principale e orchestrazione
├── models.py            # classi base e sottoclassi (OOP)
├── crud.py              # creazione, modifica, eliminazione
├── generatore.py        # generazione dati casuali
├── analytics.py         # analisi e filtri sui dati
├── export.py            # esportazione CSV
│
└── output/
    └── vendite.csv      # file generato dal programma
```

---

## Requisiti

- Python 3.10+
- Nessuna dipendenza esterna

---

## Avvio

```bash
python main.py
```

---

## Concetti OOP applicati

- Classi astratte (`ABC`, `abstractmethod`)
- Ereditarietà e override
- Polimorfismo e duck typing
- Incapsulamento (`@property`, attributi privati)
- `filter()` per l'analisi dei dati
- Moduli separati per ogni responsabilità

---

## Team

| Membro | Moduli |
|--------|--------|
| Davide Bruseghin | `models.py` |
| Gabriele De Carlo | `crud.py` · `generatore.py` |
| Manuel Cernigoj | `analytics.py` · `export.py` |

---

> Progetto in sviluppo — work in progress.