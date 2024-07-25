"""Progettare un sistema di videonoleggio con i seguenti requisiti:

1. Classe Movie:

Attributi:

    movie_id: str - Identificatore di un film.
    title: str - Titolo del film.
    director: str - Regista del film.
    is_rented: boolean - Booleano che indica se il film è noleggiato o meno.

Metodi:

    rent(): Contrassegna il film come noleggiato se non è già noleggiato. Se il film non è già noleggiato imposta is_rented a True, altrimenti stampa il messaggio "Il film {self.title} è già noleggiato."
    return_movie(): Contrassegna il film come restituito. Se il film è già noleggiato imposta is_rented a False, altrimenti stampa il messaggio "Il film {self.title} non è attualmente noleggiato."

2. Classe Customer:

Attributi:

    customer_id: str - Identificativo del cliente.
    name: str - Nome del cliente.
    rented_movies: list[Movie] - Lista dei film noleggiati.

Metodi:

    rent_movie(movie: Movie): Aggiunge il film nella lista rented_movies se non è già stato noleggiato, altrimenti stampa il messaggio "Il film {movie.title} è già noleggiato."
    return_movie(movie: Movie): Rimuove il film dalla lista rented_movies se già presente, altrimenti stampa il messaggio "Il film {movie.title} non è stato noleggiato da questo cliente."

3. Classe VideoRentalStore:

Attributi:

    movies: dict[str, Movie] - Dizionario che ha per chiave l'id del film e per valore l'oggetto Movie.
    customers: dict[str, Customer] - Dizionario che ha per chiave l'id del cliente e per valore l'oggetto Customer.

Metodi:

    add_movie(movie_id: str, title: str, director: str): Aggiunge un nuovo film nel videonoleggio se non è già presente, altrimenti stampa il messaggio "Il film con ID {movie_id} esiste già."
    register_customer(customer_id: str, name: str): Iscrive un nuovo cliente nel videonoleggio se non è già presente, altrimenti stampa il messaggio "Il cliente con ID {customer_id} è già registrato."
    rent_movie(customer_id: str, movie_id: str): Permette al cliente di noleggiare un film se entrambi esistono nel videonoleggio, altrimenti stampa il messaggio "Cliente o film non trovato."
    return_movie(customer_id: str, movie_id: str): Permette al cliente di restituire un film se entrambi esistono nel videonoleggio, altrimenti stampa il messaggio "Cliente o film non trovato."
    get_rented_movies(customer_id: str): list[Movie] - Restituisce la lista dei film noleggiati dal client (customer.rented_movies) se il cliente esiste nel videonoleggio, altrimenti stampa il messaggio "Cliente non trovato." e ritorna una lista vuota.
"""

class Movie():

    def __init__(self, movie_id: str, title: str, director: str, is_rented: bool) -> None:
        self.movie_id : str = movie_id
        self.title : str = title
        self.director : str = director
        self.is_rented : bool = False
    
    def rent(self):
        if self.is_rented is True:
            return(f"Il film {self.title} è già noleggiato")
        else:
            self.is_rented = True
    
    def return_movie(self):
        if self.is_rented is True:
            self.is_rented = False
        else:
            return(f"Il film {self.title} non è attualmente noleggiato.")

class Customer():

    def __init__(self, customer_id: str, name: str, rented_movies: list[Movie]) -> None:
        self.customer_id : str = customer_id
        self.name : str = name
        self.rented_movies : list[Movie] = []

    def rent_movie(self, movie: Movie):
        if movie.is_rented is True:
            movie.rent()
            self.rented_movies.append(movie)
        else:
            return (f"Il film {movie.title} è già noleggiato.")
        
    def return_movie(self, movie: Movie):
        if movie in self.rented_movies:
            movie.rent()
            self.rented_movies.remove(movie)
        else:
            return (f"Il film {movie.title} non è stato noleggiato da questo cliente.")
    
    
class VideoRentalStore():

    def __init__(self) -> None:
        self.movies : dict[str, Movie] = {}
        self.customers : dict[str, Customer] = {}

    def add_movie(self, movie_id: str, title: str, director: str):
        if movie_id not in self.movies:
            movie : Movie = Movie (movie_id, title,director, is_rented = False)
            self.movies[movie_id] = movie
        else:
            print(f"Il film con ID {movie_id} esiste già.")
    
    def register_customer(self, customer_id: str, name: str):
        if customer_id not in self.customers:
            customer: Customer = Customer(customer_id, name, rented_movies=[])
            self.customers[customer_id] = customer
        else:
            print(f"Il cliente con ID {customer_id} è già registrato.")

    def rent_movie(self, customer_id: str, movie_id: str):
        if customer_id in self.customers and movie_id in self.movies:
            for v in self.movies.values():
                v.rent()
                for c in self.customers.values():
                    c.rent_movie(v)
        else:
            print("Cliente o film non trovato.")

    def return_movie(self, customer_id: str, movie_id: str):
        if customer_id in self.customers and movie_id in self.movies:
            for v in self.movies.values():
                v.return_movie()
                for c in self.customers.values():
                    c.return_movie(v)
        else:
            print("Cliente o film non trovato.")

    def get_rented_movies(self, customer_id: str)->list[Movie]:
        for k,v in self.customers.items():
            if customer_id in k :
                return v.rented_movies
            else:
                print(f"Cliente non trovato. []")

    




        


        

