"""Film: Rappresenta un film con titolo e durata.
 
- Sala: Rappresenta una sala con numero identificativo, film attualmente in programmazione, posti totali, posti prenotati.

Metodi:
    - prenota_posti(num_posti): Prenota un certo numero di posti nella sala, se disponibili. Restituisce un messaggio di conferma o di errore.
    - posti_disponibili(): Restituisce il numero di posti ancora disponibili nella sala.
 
- Cinema: Gestisce le operazioni legate alla gestione delle sale.

Metodi:
    - aggiungi_sala(sala): Aggiunge una nuova sala al cinema.
    - prenota_film(titolo_film, num_posti): Trova il film desiderato e tenta di prenotare posti. Restituisce un messaggio di stato.

"""

class Film:

    def __init__(self, titolo: str, durata: float) -> None:
        self.titolo : str = titolo
        self.durata : float = durata

    def __str__(self) -> str:
        return f"film : titolo= {self.titolo}, di durata= {self.durata}"

    



class Sala:
    def __init__(self, num_sala: int, film: Film, tot_posti: int, pre_posti: int) -> None:
        self.num_sala : int = num_sala
        self.film : Film = film
        self.tot_posti : int = tot_posti
        self.pre_posti: int  = pre_posti
        
        
    def prenota_posti(self, posti: int):
        self.posti : int = posti
        if self.tot_posti - self.posti > 0:
            print("posto prenotato con successo")
        else:
            print("mi dispiace siamo al completo")
        self.pre_posti += self.posti
        return self.pre_posti

    def posti_disponibili(self):
        self.posti_liberi : int = self.tot_posti - self.pre_posti
        print(f"i posti liberi sono {self.posti_liberi}")


class Cinema(Sala):
    def __init__(self) -> None:
        self.liste_sale: list[Sala] = []
        

    def aggiuingi_sala(self, sala : Sala):
        self.sala : Sala = sala
        if sala not in self.liste_sale:
            self.liste_sale.append(sala)

    def prenota_film(self, title: str, num_posti: int):
        self.title : str = title
        self.num_posti : int = num_posti

        for sala in self.liste_sale:
            if title == sala.film.titolo:
                if num_posti <= sala.tot_posti:
                    sala.tot_posti -= num_posti
                    return f"hai prenotato con successo {num_posti} posti  per il film {title}"
                else:
                    return f"mi dispiace siamo al completo per la proiezione di {title}"
        return f"mi dispiace il film {title} non viene proiettato"
cinema1 : Cinema = Cinema()
film1 : Film = Film("Pulp Fiction",2.34)
film2 : Film = Film("Avatar", 2.21)

sala1 : Sala = Sala(14, film1, 110, 40)
sala2 : Sala = Sala(11, film2, 130, 43)
cinema1.aggiuingi_sala(sala1)
cinema1.aggiuingi_sala(sala2)
sala1.prenota_posti(23)

    
print(cinema1.prenota_film("Pulp Fiction", 20))
print(cinema1.prenota_film("L'attimo fuggente", 3))
print(cinema1.prenota_film("Avatar", 2))




"""
Gestione di un magazzino
Scrivi un programma in Python che gestisca un magazzino. Il programma deve permettere di aggiungere prodotti al magazzino, cercare prodotti per nome e verificare la disponibilità di un prodotto.

Definisci una classe Prodotto con i seguenti attributi:
- nome (stringa)
- quantità (intero)
 
Definisci una classe Magazzino con i seguenti metodi:
- aggiungi_prodotto(prodotto: Prodotto): aggiunge un prodotto al magazzino.
- cerca_prodotto(nome: str) -> Prodotto: cerca un prodotto per nome e lo ritorna se esiste.
- verifica_disponibilità(nome: str) -> str: verifica se un prodotto è disponibile in magazzino.
 
Test case:

    Un gestore del magazzino crea un magazzino e diversi prodotti in diverse quantità. Successivamente, aggiunge i prodotti al magazzino.
    Il sistema cerca un prodotto per verificare se esiste nell'inventario.
    Il sistema verifica la disponibilità dei prodotti in inventario.

"""

class Product:

    def __init__(self, name: str, quantity: int) -> None:
        self.name : str = name
        self.quantity : int = quantity

    def __str__(self) -> str:
        return f"product: {self.name}, quantity {self.quantity}"

class Store:

    def __init__(self) -> None:
        self.list_products : list[Product] = []

    def add_products(self, product: Product):
        self.product : Product = product
        if product not in self.list_products:
            self.list_products.append(product)
    
    def search_product(self, name: str):
        self.name : str = name 
        if name == self.product.name:
            return self.product.name
        
    def verify()
        