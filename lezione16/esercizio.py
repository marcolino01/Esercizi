"""Obiettivo:
Implementare una classe Media che rappresenti un media generico (ad esempio, un film o un libro) e una classe derivata Film che rappresenti specificamente un film.
 Gli studenti dovranno anche creare oggetti di queste classi, aggiungere valutazioni e visualizzare le recensioni.

Specifiche della Classe Media:
 
Attributi:
- title (stringa): Il titolo del media.
- reviews (lista di interi): Una lista di valutazioni del media, con voti compresi tra 1 e 5, dove 1=Terribile, 2=Brutto, 3=Normale, 4=Bello, 5=Grandioso.

Metodi:
- set_title(self, title): Imposta il titolo del media.
- get_title(self): Restituisce il titolo del media.
- aggiungiValutazione(self, voto): Aggiunge una valutazione alla lista delle recensioni se è valida (tra 1 e 5).
- getMedia(self): Calcola e restituisce la media delle valutazioni.
- getRate(self): Restituisce una stringa che descrive il giudizio medio basato sulla media delle valutazioni, ovvero mostra "Terribile" se il voto medio si avvicina 
a 1, "Brutto" se il voto medio si avvicina a 2, "Normale" se il voto medio si avvicina a 3, "Bello" se il voto medio si avvicina a 4, "Grandioso" se il voto medio
 si avvicina a 5.
- ratePercentage(self, voto): Calcola e restituisce la percentuale di un voto specifico nelle recensioni.
- recensione(self): Mostra un riassunto delle recensioni e delle valutazioni del media, stampando il titolo, il voto medio, il giudizio e le percentuali di ciascun
 voto. Esempio di riassunto:
 
Titolo del Film: The Shawshank Redemption
Voto Medio: 3.80
Giudizio: Bello
Terribile: 10.00%
Brutto: 10.00%
Normale: 10.00%
Bello: 30.00%
Grandioso: 40.00%

Si verifichi il funzionamento scrivendo un codice che crei almeno due oggetti di tipo Film, aggiunga a ognuno dei due almeno dieci valutazioni e richiami 
il metodo recensione()."""



class Media():

    def __init__(self, reviews: list[int] = []):
        self.titolo  = None
        self.reviews : list[int] = reviews

    def set_title(self, nuovo_titolo: str):
        self.titolo : str = nuovo_titolo
        
    def get_title(self):
        return self.titolo
    
    def aggiungiValutazione(self, voto: int):
        self.voto : int = voto
        
        if voto <= 5:
            self.reviews.append(voto)

    def getMedia(self):
        self.media : float = round(sum(self.reviews)/ len(self.reviews),2)
        return self.media
    
    def getRate(self):
        if round(self.media) == 1:
            return "Terribile"
        elif round(self.media) == 2:
            return "Brutto"
        elif round(self.media) == 3:
            return "Normale"
        elif  round(self.media) == 4:
            return "Bello"
        else:
            return "Grandioso"
    
    def ratePercentage(self, voto: int):
       i : int = self.reviews.count(voto)
       perc : float = round((i / len(self.reviews))*100, 2)
       return f"{perc}%"

    def recensione(self):
        s : str = f"Titolo del film : {self.get_title()}"
        s += f"\nVoto Medio: {self.getMedia()}"
        s += f"\nGiudizio: {self.getRate()}"
        s += f"\nTerribile: {self.ratePercentage(1)}"
        s += f"\nBrutto: {self.ratePercentage(2)}"
        s += f"\nNormale: {self.ratePercentage(3)}"
        s += f"\nBello: {self.ratePercentage(4)}"
        s += f"\nGrandioso: {self.ratePercentage(5)}"
        return s 
    
class Film(Media):
    def __init__(self, titolo: str):
        super().__init__()
        self.set_title(titolo)




        
film : Film = Film("The Shawshank Redemption")

film.aggiungiValutazione(5)
film.aggiungiValutazione(4)
film.aggiungiValutazione(5)
film.aggiungiValutazione(5)
film.aggiungiValutazione(3)
film.aggiungiValutazione(2)
film.aggiungiValutazione(5)
film.aggiungiValutazione(1)
film.aggiungiValutazione(5)
film.aggiungiValutazione(3)

print(film.recensione())



"""Vogliamo gestire un contatore che può essere incrementato, decrementato, resettato e visualizzato. La classe offre un modo semplice per tenere traccia di un 
conteggio che non può diventare negativo.

Classe Contatore
Attributi:
- conteggio: un intero che conserva il valore del conteggio, inizializzato a 0.

Metodi:
- __init__(): Inizializza l'attributo conteggio a 0.
- setZero(): Imposta il conteggio a 0.
- add1(): Incrementa il conteggio di 1.
- sub1(): Decrementa il conteggio di 1, ma non permette che il conteggio diventi negativo. Se il conteggio è già 0, stampa un messaggio di errore.
- get(): Restituisce il valore corrente del conteggio.
- mostra(): Stampa a schermo il valore corrente del conteggio."""


class Contatore:

    def __init__(self, conteggio : int = 0):
        self.conteggio : int = conteggio

    def setZero(self)-> int:
        self.conteggio : int = 0
        return self.conteggio
    
    def add1(self)-> int:
        self.conteggio +=1
        return self.conteggio
    
    def sub1(self):
        if self.conteggio >= 0:
            if self.conteggio == 0:
                print("Non è possibile eseguire la sottrazione")
            else:
                self.conteggio -=1
                return self.conteggio
    
    def get(self):
        return self.conteggio
    
    def mostra(self):
        print(f"Conteggio attuale: {self.conteggio}")
            


c = Contatore() 
c.add1()
c.add1()
c.add1()
c.add1()
c.sub1()  
c.add1()
c.add1()
z  = c.get()
print(z)


"""Sviluppa un sistema per la gestione delle ricette in Python che permetta agli utenti di creare, modificare, e cercare ricette basate sugli ingredienti. 
Il sistema dovrà essere capace di gestire una collezione di ricette e i loro ingredienti.

Classe:
- RecipeManager:
    Gestisce tutte le operazioni legate alle ricette.

    Metodi:
    - create_recipe(name, ingredients): Crea una nuova ricetta con il nome specificato e una lista di ingredienti. Restituisce un dizionario con la ricetta appena 
    creata o un messaggio di errore se la ricetta esiste già.

    - add_ingredient(recipe_name, ingredient): Aggiunge un ingrediente alla ricetta specificata. Restituisce la ricetta aggiornata o un messaggio di errore se 
    l'ingrediente esiste già o la ricetta non esiste.

    - remove_ingredient(recipe_name, ingredient): Rimuove un ingrediente dalla ricetta specificata. Restituisce la ricetta aggiornata o un messaggio di errore se 
    l'ingrediente non è presente o la ricetta non esiste.

    - update_ingredient(recipe_name, old_ingredient, new_ingredient): Sostituisce un ingrediente con un altro nella ricetta specificata. Restituisce la ricetta 
    aggiornata o un messaggio di errore se l'ingrediente non è presente o la ricetta non esiste.

    - list_recipes(): Elenca tutte le ricette esistenti.

    - list_ingredients(recipe_name): Mostra gli ingredienti di una specifica ricetta. Restituisce un elenco di ingredienti o un messaggio di errore se la ricetta 
    non esiste.

    - search_recipe_by_ingredient(ingredient): Trova e restituisce tutte le ricette che contengono un determinato ingrediente. Restituisce un elenco di ricette o 
    un messaggio di errore se nessuna ricetta contiene l'ingrediente."""


class RecipeManager:

    def __init__(self) -> None:
        self.dizrecipe : dict[str,list[str]] = {}

    def create_recipe(self, name: str, ingredients: list[str]):
        self.name : str = name
        self.ingredients : list[str] = ingredients

        if name  not in self.dizrecipe.keys():
            self.dizrecipe[name] = ingredients
            return name, ingredients
        else : 
            return "errore la recitta esiste gia"

    def add_ingredient(self,recipe_name: str, ingredient: str):
        if recipe_name in self.dizrecipe.keys():
            if ingredient not in self.dizrecipe[recipe_name]:
                self.ingredients.append(ingredient)
                return self.dizrecipe[recipe_name]
            else:
                print("l'ingrediente gia c'è")
        else:
            print("la ricetta non esiste")

    def remove_ingredient(self, recipe_name: str, ingredient: str):
        if recipe_name in self.dizrecipe.keys():
            if ingredient in self.dizrecipe[recipe_name]:
                self.ingredients.remove(ingredient)
                return self.dizrecipe[recipe_name]
            else: 
                print("non c'è questo ingrediente")
        else:
            print("non esiste la ricetta")

    def update_ingredient(self,recipe_name: str, old_ingredient: str, new_ingredient: str):
        if recipe_name in self.dizrecipe.keys():
            if old_ingredient in self.dizrecipe[recipe_name]:
                self.ingredients.remove(old_ingredient)
                self.ingredients.append(new_ingredient)
                return self.dizrecipe[recipe_name]
            else:
                return "l'ingrediente indicato non c'è"
        else:
            return "Errore non abbiamo questa ricetta"
        
    def list_recipes(self):
        self.list_recipe : list[str] = []
        for k in self.dizrecipe.keys():
            if k not in self.list_recipe:
                self.list_recipe.append(k)
            return self.list_recipe

    def list_ingredients(self, recipe_name: str):
        if recipe_name in self.dizrecipe.keys():
            return self.dizrecipe[recipe_name]
        else:
            return " Errore la ricetta non esiste"
        
    def search_recipe_by_ingredient(self, ingredient: str):
        self.search_recipe : list[str] = []
        for recipe in self.dizrecipe.keys():
            if ingredient in self.dizrecipe[recipe]:
                self.search_recipe.append(recipe)
        
        if self.search_recipe:
            return self.search_recipe
        else:
            return "non abbaimo questo ingrediente"
        
manager = RecipeManager()
print(manager.create_recipe("Pizza Margherita", ["Farina", "Acqua", "Lievito", "Pomodoro", "Mozzarella"]))
print(manager.add_ingredient("Pizza Margherita", "Basilico"))
print(manager.update_ingredient("Pizza Margherita", "Mozzarella", "Mozzarella di Bufala"))
print(manager.remove_ingredient("Pizza Margherita", "Acqua"))
print(manager.list_ingredients("Pizza Margherita"))

"""In questo esercizio, creeremo una gerarchia di classi per rappresentare diversi tipi di veicoli.
1. Classe Base: Veicolo
Crea una classe base chiamata Veicolo con i seguenti attributi e metodi:
 
Attributi:

    marca (stringa)
    modello (stringa)
    anno (intero)

Metodi:

    __init__(self, marca, modello, anno): metodo costruttore che inizializza gli attributi marca, 
    modello e anno.
    descrivi_veicolo(self): metodo che stampa una descrizione del veicolo nel formato "Marca: [marca], 
    Modello: [modello], Anno: [anno]".

2. Classe Derivata: Auto
Crea una classe derivata chiamata Auto che eredita dalla classe Veicolo e aggiunge i seguenti attributi 
e metodi:
 
Attributi:

    numero_porte (intero)

Metodi:

    __init__(self, marca, modello, anno, numero_porte): metodo costruttore che inizializza gli attributi
      della classe base e numero_porte.
    descrivi_veicolo(self): metodo che sovrascrive quello della classe base per includere anche il numero
      di porte nella descrizione, nel formato "Marca: [marca], Modello: [modello], Anno: [anno], Numero
     di porte: [numero_porte]".

3. Classe Derivata: Moto
Crea una classe derivata chiamata Moto che eredita dalla classe Veicolo e aggiunge i seguenti attributi
 e metodi:
 
Attributi:

    tipo (stringa, ad esempio "sportiva", "cruiser", ecc.)

Metodi:

    __init__(self, marca, modello, anno, tipo): metodo costruttore che inizializza gli attributi della
      classe base e tipo.
    descrivi_veicolo(self): metodo che sovrascrive quello della classe base per includere anche il 
    tipo di moto nella descrizione, nel formato "Marca: [marca], Modello: [modello], Anno: [anno], 
    Tipo: [tipo]"."""

class Veicolo:

    def __init__(self, marca: str, modello: str, anno: int):
        self.marca : str = marca
        self.modello : str = modello
        self.anno : int = anno
    def descrivi_veicolo(self):
        print(f"Marca : {self.marca}, Modello : {self.modello}, Anno : {self.anno}")
    
class Auto(Veicolo):

    def __init__(self, marca: str, modello: str, anno: int, numero_porte: int):
        super().__init__(marca, modello, anno)
        self.numero_porte : int = numero_porte

    def descrivi_veicolo(self):
        print(f"Marca : {self.marca}, Modello : {self.modello}, Anno : {self.anno}, Numero di porte {self.numero_porte}")
    
class Moto(Veicolo):

    def __init__(self, marca: str, modello: str, anno: int, tipo: str):
        super().__init__(marca, modello, anno) 
        self.tipo : str = tipo

    def descrivi_veicolo(self):
        print(f"Marca : {self.marca}, Modello : {self.modello}, Anno : {self.anno}, Tipo : {self.tipo}") 
    
veicolo = Veicolo("Generic", "Model", 2020)
auto = Auto("Toyota", "Corolla", 2021, 4)
moto = Moto("Yamaha", "R1", 2022, "sportiva")

veicolo.descrivi_veicolo()
auto.descrivi_veicolo()
moto.descrivi_veicolo()


"""Descrizione del problema
Due specie animali, i Bufali Klingon e gli Elefanti, vivono in una riserva naturale. Ogni specie ha una 
popolazione iniziale e un tasso di crescita annuo. Vogliamo sapere:
- In quanti anni la popolazione degli Elefanti supererà quella dei Bufali Klingon.
- n quanti anni la popolazione dei Bufali Klingon raggiungerà una densità di 1 individuo per km².
 
Specifiche tecniche

1. Classe Specie
- Attributi:

    nome (str): Nome della specie.
    popolazione (int): Popolazione iniziale.
    tasso_crescita (float): Tasso di crescita annuo percentuale.

- Metodi:

    __init__(self, nome: str, popolazione_iniziale: int, tasso_crescita: float): Costruttore per 
    inizializzare gli attributi della classe.
    cresci(self): Metodo per aggiornare la popolazione per l'anno successivo.
    anni_per_superare(self, altra_specie: 'Specie') -> int: Metodo per calcolare in quanti anni la 
    popolazione di questa specie supererà quella di un'altra specie.
    getDensita(self, area_kmq: float) -> int: Metodo per calcolare in quanti anni la popolazione 
    raggiungerà una densità di 1 individuo per km².

 

2. Sottoclassi BufaloKlingon e Elefante
Entrambe le sottoclassi animali BufaloKlingon ed Elefante devono ereditare dalla classe base Specie e 
devono inizializzare il nome della specie rispettiva.
 
Formule Matematiche:

    Aggiornamento della popolazione per l'anno successivo:
        Formula: popolazione_nuova = popolazione_attuale x (1 + tasso_crescita/100)
    Calcolo della densità di popolazione:
        Formula: popolazione / area_kmq
        Hint: Loop incrementale che continua ad aggiornare la popolazione finché la densità non 
        raggiunge 1 individuo per km²
    Calcolo degli anni necessari per superare la popolazione di un'altra specie:
        Hint: Loop incrementale che continua ad aggiornare la popolazione di entrambe le specie finché
          la popolazione di questa specie non supera quella dell'altra. Per evitare che le popolazioni 
          crescano all'infinito, limitare il numero di anni a 1000. """

class Specie:
    
    def __init__(self, popolazione: int, tasso_crescita: float):
        
        self.popolazione : int = popolazione
        self.tasso_crescita : float = tasso_crescita

    def cresci(self):
        self.formula_popo : float = self.popolazione * (1 + self.tasso_crescita / 100)
        return self.formula
    
    def getDensita(self, area_kmq: float):
        self.formula : float = self.popolazione / area_kmq
        anni : int = 0
        while self.formula < 1:
            self.cresci()
            anni += 1
        return anni

    
    def anni_per_superare(self, altra_specie: str):
        anni : int = 0
        while self.popolazione <= altra_specie.popolazione  and anni < 1000:
            self.cresci()
            altra_specie.cresci()
            anni += 1
        return anni
    
class BufaloKlingon(Specie):

    def __init__(self, popolazione: int, tasso_crescita: float):
        super().__init__(popolazione, tasso_crescita)

class Elefante(Specie):

    def __init__(self, popolazione: int, tasso_crescita: float):
        super().__init__( popolazione, tasso_crescita)


# Creazione delle istanze delle specie
bufalo_klingon = BufaloKlingon(100, 15)  # Crea un'istanza di BufaloKlingon con popolazione 100 e tasso di crescita 15%
elefante = Elefante(10, 35)  # Crea un'istanza di Elefante con popolazione 10 e tasso di crescita 35%


    

    
            





            
        
            
        
    



