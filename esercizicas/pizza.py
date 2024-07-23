# Sviluppa un sistema per la gestione delle ricette in Python che permetta agli utenti di creare, modificare, e cercare ricette basate sugli ingredienti. 
# Il sistema dovrà essere capace di gestire una collezione (dizionario) di ricette e i loro ingredienti.
# Classe:
# - RecipeManager:
#     Gestisce tutte le operazioni legate alle ricette.
#     Metodi
#     - create_recipe(name, ingredients): Crea una nuova ricetta con il nome specificato e una lista di ingredienti. Restituisce un nuovo dizionario con la sola ricetta appena creata o un messaggio di errore se la ricetta esiste già.
#     - add_ingredient(recipe_name, ingredient): Aggiunge un ingrediente alla ricetta specificata. Restituisce la ricetta aggiornata o un messaggio di errore se l'ingrediente esiste già o la ricetta non esiste.
#     - remove_ingredient(recipe_name, ingredient): Rimuove un ingrediente dalla ricetta specificata. Restituisce la ricetta aggiornata o un messaggio di errore se l'ingrediente non è presente o la ricetta non esiste.
#     - update_ingredient(recipe_name, old_ingredient, new_ingredient): Sostituisce un ingrediente con un altro nella ricetta specificata. Restituisce la ricetta aggiornata o un messaggio di errore se l'ingrediente non è presente o la ricetta non esiste.
#     - list_recipes(): Elenca tutte le ricette esistenti.
#     - list_ingredients(recipe_name): Mostra gli ingredienti di una specifica ricetta. Restituisce un elenco di ingredienti o un messaggio di errore se la ricetta non esiste.
#     - search_recipe_by_ingredient(ingredient): Trova e restituisce tutte le ricette che contengono un determinato ingrediente. Restituisce un elenco di ricette o un messaggio di errore se nessuna ricetta contiene l'ingrediente.

class RecipeManager():

    def __init__(self) -> None:
        self.ricette : dict[str, list[str]] = {}

    def create_recipe(self,name: str, ingredients: list[str])->dict[str,list[str]]:
        if name not in self.ricette:
            self.ricette[name] = ingredients
            return self.ricette
        else :
            return "La ricetta esiste già"
    
    def add_ingredient(self, recipe_name: str, ingredient: str):
        if recipe_name in self.ricette and ingredient not in self.ricette[recipe_name]:
            self.ricette[recipe_name].append(ingredient)
            return self.ricette
        else:
            return "Errore l'ingrediente è già presente nella ricetta"
        
    def remove_ingredient(self, recipe_name: str, ingredient: str):
        if recipe_name in self.ricette:
            if ingredient in self.ricette[recipe_name]:
                self.ricette[recipe_name].remove(ingredient)
                return self.ricette
            else:
                return "L'ingrediente non è presente nella ricetta"
        else:
            return "Errore la ricetta non esiste"
    
    def update_ingredient(self, recipe_name: str, old_ingredient: str, new_ingredient: str):
        if recipe_name


            
    