"""Classi:
- Libro: Rappresenta un libro con titolo, autore, stato del prestito. Il libro deve essere 
inizialmente disponibile (non prestato).
- Biblioteca: Gestice tutte le operazioni legate alla gestione di una biblioteca.

    Metodi:
    - aggiungi_libro(libro): Aggiunge un nuovo libro al catalogo della biblioteca. Restituisce 
    un messaggio di conferma.
    - presta_libro(titolo): Cerca un libro per titolo e, se disponibile e non già prestato, 
    lo segna come disponibile. Restituisce un messaggio di stato.
    - restituisci_libro(titolo): Cerca un libro per titolo e, se trovato e prestato, lo segna 
    come disponibile. Restituisce un messaggio di stato.
    - mostra_libri_disponibili(): Restituisce una lista dei titoli dei libri attualmente disponibili.
    Se non ci sono libri disponibili, restituisce un messaggio di errore."""

class Libro:
    def __init__(self, title: str, author: str, borrowed : bool = False) -> None:
        self.title : str = title
        self.author : str = author
        self.borrowed : bool = borrowed

    def __str__(self) -> str:
        return f"Book: title: {self.title}, author: {self.author}, borrowed: {self.borrowed}"
    
class Biblioteca:

    def __init__(self) -> None:
        self.list_book : list[Libro] = []

    def aggiungi_libro(self, libro : Libro):
        self.libro : Libro = libro
        if libro not in self.list_book:
            self.list_book.append(libro)
        return self.list_book
    
    def presta_libro(self, titolo: str):
        for i in self.list_book:
            if titolo == i.title:
                if i.borrowed != True:
                    i.borrowed = True
                    return f"il libro {titolo} è disponibile"
                else:
                    return f"il libro {titolo} è stato già prestato"
            return f"il libro {titolo} non è disponibile"
            
    def restituisci_libro(self, titolo: str):   
        for book in self.list_book:
            if titolo == book.title:
                if book.borrowed == True:
                    book.borrowed = False
                    return f"il libro {titolo} è stato restituito correttamente"
            return f"il libro {titolo} non è stato prestato"
       
        
    def mostra_disponibili(self):
        self.lista_disponibili : list[str] = []
        for book in self.list_book:
            if book.borrowed is False:
                self.lista_disponibili.append(book.title)
        return f"ecco la lista dei libri disponibili {self.lista_disponibili}"
            
            
        
    
        
libro1 : Libro = Libro("io uccido", "Giorgio Faletti", False)
libro2 : Libro = Libro("io sono dio","Giorgio Faletti", False)
libro3 : Libro = Libro("la lunga marcia","Stephen King", False)
biblioteca1 : Biblioteca = Biblioteca()
biblioteca1.aggiungi_libro(libro1)
biblioteca1.aggiungi_libro(libro2)
biblioteca1.aggiungi_libro(libro3)
print(biblioteca1.presta_libro("io uccido"))
print(biblioteca1.restituisci_libro("io uccido"))
#print(biblioteca1.mostra_disponibili())


"""Sviluppa un sistema in Python per la gestione di un catalogo film che permetta di aggiungere, 
rimuovere e cercare film di un particolare regista. Il sistema dovrebbe consentire anche di 
visualizzare tutti i registi e i loro film.
Classe:
- MovieCatalog: Gestisce tutte le operazioni legate al catalogo dei film.
    Metodi:
    - add_movie(director_name, movies): Aggiunge uno o più film a un regista specifico nel catalogo. 
    Se il regista non esiste, viene creato un nuovo record. Se il regista esiste, la sua lista di film
     viene aggiornata.
    - remove_movie(director_name, movie_name): Rimuove un film specifico dall'elenco dei film di 
    un regista. Se tutti i film sono rimossi, il regista può essere opzionalmente rimosso dal catalogo.
    - list_directors(): Elenca tutti i registi presenti nel catalogo.
    - get_movies_by_director(director_name): Restituisce tutti i film di un regista specifico.
    - search_movies_by_title(title): Trova tutti i film che contengono una certa parola nel titolo.
      Restituisce un elenco dei registi e dei rispettivi film che contengono la parola cercata o un 
      messaggio di errore se nessun film contiene la parola cercata nel titolo."""

    
class MovieCatalog():

    def __init__(self) -> None:
        self.moviedict: dict[str,list[str]] = {}

    def __str__(self) -> str:
        return f"MovieCatalog : {self.moviedict}"

    def add_movie(self, director_name: str, movies: list[str]):
        self.director_name : str = director_name
        self.movie : list[str] = movies
        if director_name in self.moviedict:                                
            self.moviedict[director_name].extend(movies)
        else:
            self.moviedict[director_name] = movies
        
    def remove_movie(self, director_name: str, movie_name: str):
        self.director_name : str = director_name
        self.movie_name : str = movie_name
        if director_name in self.moviedict:
            try:
                self.moviedict[director_name].remove(movie_name)
                if not self.moviedict:
                    del self.moviedict[director_name]
            except ValueError:
                print(f"Non c'è questo film {movie_name} per questo regista")
        else:
            print(f"il regista {director_name} non è presente nel nostro cataologo")

    def list_directors(self):
        self.listdirector : list[str] = []
        for k in self.moviedict.keys():     
            self.listdirector.append(k)
        return self.listdirector
        #return list(self.moviedict.keys()) --> potevo scrivere anche cosi
    
    def get_movies_by_director(self,director_name: str):
        for k,v in self.moviedict.items():
            if director_name == k:
                return v
    
    def search_movies_by_title(self, title:str ):
        self.title : str = title
        for director in self.moviedict.keys():
            for movie in self.moviedict.values():
                if title in movie:
                    return movie




            
    

        
catalog = MovieCatalog()
catalog.add_movie("Quentin Tarantino", ["Pulp Fiction", "Kill Bill", "Django Unchained"])
catalog.add_movie("Christopher Nolan", ["Inception", "Dunkirk", "Interstellar"])
print(catalog)
print(catalog.list_directors())
catalog.remove_movie("Christopher Nolan","Dunkirk")
print(catalog)
print(catalog.get_movies_by_director("Christopher Nolan"))

print(catalog.search_movies_by_title("Bill"))


def fibonacci(i: int):
    a : int = 1
    b : int = 1

    for _ in range(i):
        c = a + b
        a = b
        b = c
    return b

import time
a = time.time()

print(fibonacci(52))
print(f"tempo impiegato : {time.time()- a}")