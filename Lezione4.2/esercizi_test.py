""""Nel gioco del blackjack, il valore di una mano è determinato dalla somma dei valori delle carte. Ogni carta ha un valore compreso tra 2 e 
11 compresi. Tuttavia, se una mano contiene un asso, il valore dell'asso può essere 1 o 11, a seconda di quale sia più favorevole al giocatore in quel 
momento. Dato un elenco di valori delle carte che rappresentano una mano di blackjack, scrivi una funzione per determinare il valore totale della mano."""

def blackjack(cards: list[int])->int:
    cards_sum: int = sum(cards)
    num_aces : int = cards.count(1) + cards.count(11)

    while cards_sum > 21 and num_aces > 0:
        cards_sum -= 10
        num_aces -= 1
    
    return cards_sum

print(blackjack([10,1,5]))


"""Uno sviluppatore web deve sapere come progettare le dimensioni di una pagina web. Pertanto, data l'area specifica di una pagina Web rettangolare, 
il tuo compito ora è progettare una pagina Web rettangolare, la cui lunghezza L e larghezza W soddisfino i seguenti requisiti:

1. L'area della pagina web rettangolare che hai progettato deve essere uguale all'area di destinazione specificata.
2. La larghezza W non deve essere maggiore della lunghezza L, il che significa L >= W.
3. La differenza tra la lunghezza L e la larghezza W dovrebbe essere la minima possibile.

Restituisce una lista [L, W] dove L e W sono la lunghezza e la larghezza della pagina web che hai progettato in sequenza.

Esempio:

construct_rectangle(4)

L'area target è 4 e tutti i modi possibili per costruirla sono [1,4], [2,2], [4,1].
Ma secondo il requisito 2, [1,4] è illegale; secondo il requisito 3, [4,1] non è ottimale rispetto a [2,2]. Quindi la lunghezza L è 2 e la larghezza W è 2."""

def construct_rectangle(area: float)-> list[float]:
    combos : list[int] = []
    half_area : int = int(area ** 0.5)
    for width in range(1, area + 1):
        for height in range(1, half_area + 1):
            if width * height == area and width >= height:
                combos.append([width, height])

    min_diff: float =  float('inf')
    index_diff: int = 0
    for i, combo in enumerate(combos):
        curr_diff: float = combo[0] - combo[1]
        if curr_diff <= min_diff:
            min_diff = curr_diff
            index_diff = i
    return combos[index_diff]


def construct_rectangle_optimazed(area :float)-> list[int]:
    sqrt_area = int (area ** 0.5)
    for height in range(sqrt_area, 0, -1):
        if area % height == 0:
            width = area // height
            return [width, height]
        

"""Scrivi una funzione che accetta una stringa come input, rimuove le parole non significative comuni stop_words e restituisce un dizionario in cui le 
chiavi sono parole univoche nel testo rimanente (ignorando la distinzione tra maiuscole e minuscole e la punteggiatura) e i valori sono le frequenze di
quelle parole."""


stopwords = ['the', 'and', 'is', 'in', 'on', 'of']
text = "The quick brown fox jumps over the lazy dog. The dog is very lazy."

import re
def word_frequency(text : str, stopwords: list[str])-> dict[str, int]:
    text = re.sub(r'[^\w\s]', '', text.lower())

    words = list()
    for word in text:
        if word not in stopwords:
            words.append(word)
    
    result = {}                                          # from collections import Counter
    for word in words:
        if word not in words:                                   #result = Counter(words)
            result[word] = 1
        else :                                               #return dict(result)
            result[word] += 1
    return result



print(word_frequency(text, stopwords))


"""Immagina di avere una raccolta di note musicali rappresentate da una serie di numeri interi. Queste note possono avere altezze (valori) diversi. 
Una sequenza armoniosa è come una melodia piacevole in cui la differenza di altezza tra la nota massimale e quella minimale è uguale a 1. Ad esempio, 
la serie di note [3,2,2,2,3] è armoniosa, perché la differenza fra 3 e 2 è 1.

Trovare l'armonia perfetta:

Il tuo compito è scrivere una funzione che prenda come input questa serie di note musicali (numeri). La funzione dovrebbe trovare 
la sequenza armoniosa più lunga che puoi creare da queste note. Ricorda, una sottosequenza è una selezione di note dalla lista originale che mantiene 
l'ordine degli elementi.

Colpire le note giuste:

Ad esempio, se nums è [1, 3, 2, 2, 5, 2, 3, 7], la sottosequenza armonica più lunga è [3, 2, 2, 2, 3]. La funzione dovrebbe restituire 5 
(la lunghezza di questa sottosequenza)."""

from collections import Counter
def find_lhs(notes: list[int]) -> int:
    num_freq = dict(Counter(notes))

    max_lenght = 0
    
    for num in num_freq:
        if num + 1 in num_freq:
            somma = num_freq[num] + num_freq[num + 1]
            if somma >= max_lenght:
                max_lenght = somma
           # max_lenght = max(max_lenght, num_freq[num] + num_freq[num+1])

    return max_lenght 


print(find_lhs([1,3,2,2,5,2,3,7]))
print(find_lhs([1,2,3,4]))




"""Immagina di avere uno scrigno pieno di gioielli (rappresentati da una lista di numeri interi). Questi gioielli hanno vari valori, alcuni più preziosi di 
altri. Il tuo compito è trovare il terzo gioiello distinto più prezioso nello scrigno.

Qual è la svolta?

Nello scrigno possono esserci gioielli duplicati (numeri con lo stesso valore). A noi però interessano solo valori distinti, ovvero gioielli con valori unici.

Scrivi una funzione che prenda come input questo array di valori di gioielli (numeri). Se nello scrigno sono presenti almeno tre valori distinti, la funzione
 dovrebbe restituire il valore del terzo gioiello distinto di maggior valore.

Ma c'è un problema!

Se non ci sono tre valori distinti (ad esempio, solo due valori univoci o tutti i valori sono uguali), la funzione dovrebbe restituire il valore del 
gioiello più prezioso nello scrigno."""

def third_max(gems: list[int]) -> int:
    gems = sorted(list(set(gems)), reverse = True)
    if len(gems) >= 3:
        return gems[2]
    else:
        return gems[0]
    

print(third_max([3, 2, 1]))
print(third_max([1, 2]))
print(third_max([2, 2, 3, 1]))


"""Sei un detective esperto nel mondo dei testi e un caso sconcertante è arrivato sulla tua scrivania. Due stringhe, s e t, sono i tuoi sospettati. 
La tua missione: determinare se s si nasconde in bella vista all'interno di t, ma con una svolta!
Qual è il problema?
Non puoi semplicemente confrontare le stringhe lettera per lettera. Immagina che s sia un personaggio subdolo che cerca di confondersi tra la folla (t).
 Potrebbero camuffarsi nascondendosi tra altri personaggi, ma non cambiano mai il loro ordine! Quindi, "ace" può intrufolarsi in "abcde" (rimuove semplicemente
   "b" e "d"), ma "aec" non funzionerebbe (l'ordine cambia).
Scrivi una funzione di interruzione del codice che prenda la stringa s (il carattere subdolo) e t (la folla) come input. 
Se è possibile trovare s in agguato all'interno di t mantenendo il suo travestimento (ordine), restituisce True. Altrimenti restituisce False.
 Dimostra le tue abilità da detective e svela la verità nascosta!"""

def is_subsequence(s: str, t: str) -> bool:
    if s == "":
        return True
    

    s_pointer : int = 0
    t_pointer : int = 0

    while s_pointer < len(s) and t_pointer(t):
        if s[s_pointer] == t[t_pointer]:
            s_pointer += 1
        t_pointer +=1
    return s_pointer == len(s)
    



print(is_subsequence("abc", "ahbgdc"))
print(is_subsequence("axc", "ahbgdc"))
