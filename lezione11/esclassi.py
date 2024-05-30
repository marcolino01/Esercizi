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
        self.liste_sale: list[int] = []
        

    def aggiuingi_sala(self, sala : Sala):
        self.sala : Sala = sala
        if sala not in self.liste_sale:
            self.liste_sale.append(sala)

    def prenota_film(self, title: str, num_posti: int):
        self.title : str = title
        self.num_posti : int = num_posti

        for sala in self.liste_sale:
            if title == sala.film.titolo and num_posti <= self.posti_liberi:
                print(f"hai prenotato con successo i tuoi posti per il film {title}")
            else:
                print(f"mi dispiace siamo al completo xxxxx")
cinema1 : Cinema = Cinema()
film1 : Film = Film("Pulp Fiction",2.34)
film2 : Film = Film("Avatar", 2.21)

sala1 : Sala = Sala(14, film1, 110, 40)
cinema1.aggiuingi_sala(sala1)
sala1.prenota_posti(23)

    
cinema1.prenota_film("Pulp Fiction", 20)