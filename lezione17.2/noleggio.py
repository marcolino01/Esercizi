from film import Film
from moviw_genre import Commedia, Dramma, Azione

class Noleggio:

    def __init__(self, film_list: list[Film], rented_film: dict[int,list[Film]]):
        self.film_list : list[Film] = film_list
        self.rented_film : dict[int,list[Film]] = rented_film
        self.rented_film = {}
        self.film_noleggio : list[Film] = []

    def isAvailable(self, film : Film):
            
        for movie in self.film_list:
            if film.isEqual(movie):
            print(f"Il film scelto è disponibile: {film.getTitle()}!")
            return True
        else : 
            print(f"Il film scelto non è disponibile: {film.getTitle()}!")
            return False
    
    def rentAMovie(self, film: Film, clientID: int):

        if self.isAvailable(film) == True:
            self.film_list.remove(film)
            self.film_noleggio.append(film)
            self.rented_film[clientID] = self.film_noleggio
            print(f"Il cliente {clientID} ha noleggiato {film.getTitle()}!")
        else:
            print(f"Non è possibile nolegiare il film {film.getTitle()}!")

    def giveBack(self, film: Film, clientID: int, days: float):

        if clientID in self.rented_film.keys():
            if film in self.rented_film[clientID]:
                self.film_noleggio.remove(film)
                self.film_list.append(film)
                tot: float = film.calcolaPenaleRitardo(days)
                print(f"Cliente:{clientID}!La penale da pagare per il film {film} è di {tot}")
        
    def printMovies(self):
        pass

    def printRentMovies(self, clientID: int):

        if clientID in self.rented_film.keys():
            print (self.rented_film[clientID])

    