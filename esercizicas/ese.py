"""Scrivi una funzione che ruota gli elementi di una lista verso sinistra di un numero specificato
 k di posizioni. La rotazione verso sinistra significa che ciascun elemento della lista viene 
 spostato a sinistra di una posizione e l'elemento iniziale viene spostato alla fine della lista. 
 Per la rotazione utilizzare lo slicing e gestire il caso in cui il numero specificato di posizioni 
 sia maggiore della lunghezza della lista. 
For example:

Test    Result
print(rotate_left([1, 2, 3, 4, 5], 2))
[3, 4, 5, 1, 2]"""

def ruota_elementi(lista: list[int], k: int):
    n : int = len(lista)
    
    if k > n :
        k = k % n
    ruotati  = lista[k:] + lista[:k]
    return ruotati
print(ruota_elementi([1, 2, 3, 4, 5], 2))


################################################
# Scrivi una funzione che unisce due dizionari. Se una chiave è presente in entrambi, 
# somma i loro valori.
#For example:

"""Test    Result
print(merge_dictionaries({'x': 5}, {'x': -5}))
{'x': 0}

Test    Expected    Got
print(merge_dictionaries({'a': 1, 'b': 2}, {'b': 3, 'c': 4}))
{'a': 1, 'b': 5, 'c': 4}
{'a': 1, 'b': 5, 'c': 4}
print(merge_dictionaries({}, {'a': 10, 'b': 20}))
{'a': 10, 'b': 20}
{'a': 10, 'b': 20}
print(merge_dictionaries({'x': 5}, {'x': -5}))
{'x': 0}
{'x': 0}
print(merge_dictionaries({}, {}))
{}
{}
print(merge_dictionaries({'a': 3}, {'b': 4}))
{'a': 3, 'b': 4}
{'a': 3, 'b': 4}"""
def merge_dictionaries(diz1: dict[str, int], diz2: dict[str,int]):
    
    for k,v in diz2.items():
        if k in diz1.keys():
            diz1[k] += v
        else:
            diz1[k] = v
    return diz1
print(merge_dictionaries({'a': 1, 'b': 2}, {'b': 3, 'c': 4}))

#############Scrivi una funzione che elimini dalla lista dati certi elementi 
# specificati in un dizionario. Il dizionario contiene elementi da rimuovere come chiavi 
# e il numero di volte che devono essere rimossi come valori.
"""For example:

Test    Result
print(rimuovi_elementi([1, 2, 3, 2, 4], {2: 2}))
[1, 3, 4]
print(rimuovi_elementi([], {2: 1})) 
[]"""
def rimuovi_elementi(lista : list[int], diz1 : dict[int,int]):
    for k,v in diz1.items():
        if k in lista:
            for _ in range(v):
                lista.remove(k)
            return lista
print(rimuovi_elementi([1, 2, 3, 2, 4], {2: 2}))
##################

"""Scrivi una funzione che accetti un dizionario di prodotti con i prezzi e restituisca
 un nuovo dizionario con solo i prodotti che hanno un prezzo superiore a 20, scontati del 10%.
For example:

Test    Result
print(filtra_e_mappa({'Penna': 15.0, 'Zaino': 50.0, 'Quaderno': 22.0}))
{'Zaino': 45.0, 'Quaderno': 19.8}
print(filtra_e_mappa({'Gomma': 2.0, 'Matita': 1.0}))"""

def filtra_e_mappa(diz1: dict[str,float]):
    for k,v in diz1.items():
        if v > 20.0:
            diz1[k] = v-(v*10)/100
    return diz1
print(filtra_e_mappa({'Penna': 15.0, 'Zaino': 50.0, 'Quaderno': 22.0}))






