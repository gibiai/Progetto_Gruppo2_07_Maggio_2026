# 🧵 Sartoria Elegante — Gestione Intelligente di una Sartoria

## 👥 Team Project Collaboration

Progetto sviluppato in gruppo per applicare i principi della Programmazione Orientata agli Oggetti attraverso collaborazione e suddivisione logica dei compiti.

**Team Members:**
- Davide Bruseghin
- Manuel Cernigoj
- Gabriele De Carlo

---

## 🎯 Obiettivi del Progetto

- Modellare due famiglie di oggetti: **Capi Principali** (Giacca, Pantalone, Gilet) e **Componenti di Finitura** (Cravatta, Papillon, Pochette)
- Applicare i principi fondamentali della Programmazione Orientata agli Oggetti
- Gestire un catalogo di articoli sartoriali tramite operazioni CRUD (crea, modifica, elimina)
- Simulare vendite casuali realistiche e analizzarne i dati
- Utilizzare il **polimorfismo** tramite `.descrivi()` e `.get_tipo()` su oggetti di tipo diverso
- Esportare i dati su file CSV per la persistenza

---

## 🛠️ Tech Stack

- Python 3.10+
- OOP (Encapsulation, Inheritance, Polymorphism, Abstraction)
- `ABC` e `@abstractmethod` per le classi astratte
- Liste e gestione oggetti in memoria
- Modulo `csv` per l'esportazione
- Modulo `random` per la generazione dati

---

## 📂 Project Structure

- `models.py` — Classi astratte base e sottoclassi (Davide)
- `crud.py` — Operazioni CRUD sul catalogo (Gabriele)
- `generatore.py` — Simulazione vendite casuali (Gabriele)
- `analytics.py` — Analisi e statistiche sulle vendite (Manuel)
- `export.py` — Esportazione CSV (Manuel)
- `main.py` — Entry point e menu principale (Davide)

---

## ⚙️ Setup

- Nessuna dipendenza esterna necessaria
- Eseguire con `python3 main.py`

---

## 🧱 Core Classes

**Prima famiglia — Capi Principali:**
- `CapoPrincipale` — classe astratta con `@abstractmethod` su `descrivi()` e `get_tipo()`
- `Giacca` — sottoclasse con attributo specifico `numero_bottoni`
- `Pantalone` — sottoclasse con attributo specifico `tipo_taglio`
- `Gilet` — sottoclasse con attributo specifico `revers_presente`

**Seconda famiglia — Componenti di Finitura:**
- `ComponenteDiFinitura` — classe astratta con `@abstractmethod` su `descrivi()` e `get_tipo()`
- `Cravatta` — sottoclasse con attributo specifico `larghezza`
- `Papillon` — sottoclasse con attributo specifico `tipo_chiusura`
- `Pochette` — sottoclasse con attributo specifico `piega_decorativa`

**Moduli funzionali:**
- `crud.py` — `crea_capo()`, `crea_componente()`, `modifica_capo()`, `elimina_capo()`, `visualizza_tutti()`
- `generatore.py` — `genera_dati()` con banche dati di valori realistici e lista globale `vendite[]`
- `analytics.py` — `analizza_tutti()`, `analizza_per_tipo()`, `analizza_per_tipo_e_personalizzazione()`, `analizza_attributi()`
- `export.py` — `esporta_csv()` con calcolo fatturato al momento della scrittura

---

## 📊 Functional Workflow

1. Avvio del programma e generazione automatica dati di esempio
2. Inserimento manuale di capi o componenti tramite menu CRUD
3. Generazione vendite casuali con `genera_dati()` — usa i capi già inseriti come base
4. Analisi delle vendite tramite sottomenu dedicato (tutti, per tipo, per personalizzazione)
5. Esportazione del registro vendite su `vendite.csv`

---

## 📈 Key Learning Outcomes

1. **Incapsulamento** — ogni modulo gestisce la propria responsabilità, le liste vivono nel `main` e vengono passate come parametri
2. **Ereditarietà** — le sottoclassi ereditano attributi e costruttore dalla classe base tramite `super()`
3. **Polimorfismo** — `.descrivi()` e `.get_tipo()` overridati in ogni sottoclasse producono output diversi sullo stesso ciclo `for`
4. **Astrazione** — `CapoPrincipale` e `ComponenteDiFinitura` sono classi astratte (`ABC`) che non si possono istanziare direttamente
5. **Modularità** — ogni file ha un compito specifico e comunica con gli altri tramite import

---

## 📄 License

This project is intended for educational purposes and practical OOP training.
