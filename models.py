from abc import ABC, abstractmethod

class CapoPrincipale(ABC): # creazione della prima famiglia con gli attributi indicati nella traccia
    def __init__(self, codice, nome, tessuto, colore, taglia, prezzo):
        self.codice = codice
        self.nome = nome
        self.tessuto = tessuto
        self.colore = colore
        self.taglia = taglia
        self.prezzo = prezzo

    @abstractmethod # metodi astratti da passare alle sottoclassi
    def descrivi(self):
        pass

    @abstractmethod
    def get_tipo(self):
        pass
    
class Giacca(CapoPrincipale): # creazione sottoclesse giacca con attributi ereditati e uno proprio
    def __init__(self, codice, nome, tessuto, colore, taglia, prezzo, numero_bottoni):
        super().__init__(codice, nome, tessuto, colore, taglia, prezzo)
        self.numero_bottoni = numero_bottoni

    def descrivi(self): # metodo descrittivo del prodotto
        print(f"[{self.codice}] GIACCA - {self.nome} | {self.tessuto} | "
              f"{self.colore} | Taglia: {self.taglia} | €{self.prezzo:.2f}")
        print(f"  → Bottoni: {self.numero_bottoni}")

    def get_tipo(self):
        return "Giacca"


class Pantalone(CapoPrincipale): # creazione sottoclasse pantalone con attributi ereditati e uno proprio
    def __init__(self, codice, nome, tessuto, colore, taglia, prezzo, tipo_taglio):
        super().__init__(codice, nome, tessuto, colore, taglia, prezzo)
        self.tipo_taglio = tipo_taglio

    def descrivi(self): # metodo descrittivo del prodotto
        print(f"[{self.codice}] PANTALONE - {self.nome} | {self.tessuto} | "
              f"{self.colore} | Taglia: {self.taglia} | €{self.prezzo:.2f}")
        print(f"  → Tipo taglio: {self.tipo_taglio}")

    def get_tipo(self):
        return "Pantalone"


class Gilet(CapoPrincipale): # creazione sottoclasse gilet con attributi ereditati e uno proprio
    def __init__(self, codice, nome, tessuto, colore, taglia, prezzo, revers_presente):
        super().__init__(codice, nome, tessuto, colore, taglia, prezzo)
        self.revers_presente = revers_presente

    def descrivi(self): # metodo descrittivo con aggiunta di presenza dell'attributo proprio
        revers = "Sì" if self.revers_presente else "No"
        print(f"[{self.codice}] GILET - {self.nome} | {self.tessuto} | "
              f"{self.colore} | Taglia: {self.taglia} | €{self.prezzo:.2f}")
        print(f"  → Revers: {revers}")

    def get_tipo(self):
        return "Gilet"
    
class ComponenteDiFinitura(ABC): # creazione seconda famiglia con attributi indicati nella traccia
    def __init__(self, codice, nome, materiale, colore, prezzo):
        self.codice = codice
        self.nome = nome
        self.materiale = materiale
        self.colore = colore
        self.prezzo = prezzo

    @abstractmethod
    def descrivi(self):
        pass

    @abstractmethod
    def get_tipo(self):
        pass
    
class Cravatta(ComponenteDiFinitura): # sottoclasse cravatta con attributi ereditati e propri
    def __init__(self, codice, nome, materiale, colore, prezzo, larghezza):
        super().__init__(codice, nome, materiale, colore, prezzo)
        self.larghezza = larghezza

    def descrivi(self):
        print(f"[{self.codice}] CRAVATTA - {self.nome} | {self.materiale} | "
              f"{self.colore} | €{self.prezzo:.2f}")
        print(f"  → Larghezza: {self.larghezza} cm")

    def get_tipo(self):
        return "Cravatta"
    
class Papillon(ComponenteDiFinitura): # sottoclasse papillon con attributi ereditati e proprio
    def __init__(self, codice, nome, materiale, colore, prezzo, tipo_chiusura):
        super().__init__(codice, nome, materiale, colore, prezzo)
        self.tipo_chiusura = tipo_chiusura

    def descrivi(self):
        print(f"[{self.codice}] PAPILLON - {self.nome} | {self.materiale} | "
              f"{self.colore} | €{self.prezzo:.2f}")
        print(f"  → Tipo chiusura: {self.tipo_chiusura}")

    def get_tipo(self):
        return "Papillon"
    
class Pochette(ComponenteDiFinitura): # sottoclasse pochette con attributi ereditati e propri
    def __init__(self, codice, nome, materiale, colore, prezzo, piega_decorativa):
        super().__init__(codice, nome, materiale, colore, prezzo)
        self.piega_decorativa = piega_decorativa

    def descrivi(self):
        print(f"[{self.codice}] POCHETTE - {self.nome} | {self.materiale} | "
              f"{self.colore} | €{self.prezzo:.2f}")
        print(f"  → Piega decorativa: {self.piega_decorativa}")

    def get_tipo(self): 
        return "Pochette" 
