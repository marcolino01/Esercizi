"""Scrivere il frammento di codice che cambi il valore intero memorizzato nella variabile x nel seguente modo:
- se x è pari, deve essere diviso per 2;
- se x è dispari deve essere moltiplicato per 3 e gli deve essere sottratto 1."""
"""x : int = int(input("inserisci un numero:"))
if x % 2 == 0 :
    x = x / 2
else:
    x = x * 3 + 1
print(x)"""

"""Sviluppare una funzione in Python per calcolare lo stipendio lordo di ciascuno dei diversi impiegati. 
L'azienda paga 10 dollari all'ora per le prime 40 ore di lavoro e paga "una volta e mezza" la paga 
oraria per tutte le ore di lavoro oltre le 40 ore.
 
Per ogni operaio, viene fornito il numero di ore che tale impiegato ha lavorato durante la settimana.
La vostra funzione deve ricevere questa informazione per ogni impiegato e determinare e stampare lo 
stipendio lordo."""

from cmath import sqrt
import math


ore_lavorate = 41
paga = ore_lavorate * 10
if ore_lavorate <= 40:
    paga = paga
else:
    ore_inpiu = ore_lavorate - 40
    straordinario = ore_inpiu * 15
    paga += straordinario


"""Scrivere in Python dei cicli che stampino le seguenti sequenze di valori:
a) 1, 2, 3, 4, 5, 6, 7
b) 3, 8, 13, 18, 23
c) 20, 14, 8, 2, -4, -10
d) 19, 27, 35, 43, 51"""


"""for i in range (1,8):
    print(i)
for i in range (3, 24, 5):
    print(i)
for i in range (20, -11, -6):
    print(i)
for i in range (19, 52, 8):
    print(i)"""

"""Scrivere una funzione chiamata integerPower che, dati in input una base e un esponente, 
restituisca il risultato della potenza base^exponent. Supporre che base sia un numero intero e 
che l'esponente sia un valore intero positivo e diverso da 0.
 
La funzione deve usare un ciclo come struttura di controllo per il calcolo del risultato.
Non utilizzare nessuna funzione della libreria math!"""
def integerPower(x: int, y: int) -> int:
    z = 1
    while y != 0:
        z *= x
        y -=1
    return z

print(integerPower(3,4))


"""Definire una funzione chiamata hypotenuse che calcoli la lunghezza dell'ipotenusa di un 
triangolo rettangolo. La funzione deve ricevere due argomenti di tipo float 
(corrispondenti ai due lati del triangolo) e restituire l'ipotenusa come un float."""

def hypotenuse(lato1: float, lato2: float):
    ipo = ((lato1*lato1) + (lato2*lato2))** 0.5
    return ipo

print(hypotenuse(3,4))





"""Scrivi una funzione che rimuove tutti i duplicati da una lista, contenente sia numeri che lettere, mantenendo l'ordine originale degli elementi."""
def remove_duplicates(lista1: list) -> list:
    lista : list = []

    for i in lista1:
        if i not in lista:
            lista.append(i)
    return lista
    




"""Scrivere la funzione chiamata seconds_since_noon che riceva il tempo espresso come tre argomenti interi (ore, minuti e secondi) e restituisca il 
numero dei secondi da quando l'orologio "ha battuto le 12" l'ultima volta (le ore 12, dunque, vengono considerate come orario di partenza, dunque, come uno zero).

Ad esempio, alle ore 3:15:50 sono passate 3 ore, 15 minuti e 50 secondi, ovvero sono passati 11750 secondi da quando l'orologio ha "battuto le 12" per 
l'ultima volta.

Definire, poi, la funzione chiamata time_difference che prende come argomento due orari, entrambi espressi mediante ore, minuti e secondi. 
La funzione time_difference deve usare la funzione seconds_since_noon per calcolare la quantità di tempo in secondi tra due orari, entrambi contenuti entro un 
ciclo dell'orologio di 12 ore.

Ad esempio, tra le ore 1:00 e 3:15:30 sono passati 8130 secondi."""


def seconds_since_noon(hours: int, min: int, seconds: int) -> int:
    if hours >12 :
        hours -= 12
        tot_sec : int = hours*60*60 + min*60 + seconds
    else:
        tot_sec : int = hours*60*60 + min*60 + seconds
    
    return tot_sec

def time_difference(h1: int, m1: int, s1: int, h2: int, m2: int, s2: int)-> int:
    time1 : int = seconds_since_noon(h1, m1, s1)
    time2 : int = seconds_since_noon(h2, m2, s2)
    if time1 >= time2:
        result : int = time1 - time2
    else:
        result : int = time2 - time1

    return result

"""
Si scriva una funzione in Python che simuli una palla che rimbalza calcolando la sua altezza da terra in centimetri per ogni secondo, a mano a mano che 
il tempo passa su un orologio simulato.

Al tempo zero la palla comincia ad altezza zero e ha una velocità iniziale di 100 cm/s.

Dopo ogni secondo, il valore dell'altezza cambia, aggiungendo al valore corrente dell'altezza il valore della velocità corrente; poi, il valore della velocità 
viene modificato, sottraendo 96 al valore della velocità corrente.
Dunque, dopo ogni secondo, si ha che
altezza = altezza + velocità
velocità = velocità - 96.
 
Se il nuovo valore che si ottiene per l'altezza è inferiore a 0, si deve moltiplicare altezza e velocità per -0.5 per simulare il rimbalzo. Dunque, per il rimbalzo, 
si avrà che
altezza= altezza*-0,5 
velocità=velocità*-0,5.

Ci si fermi al quinto rimbalzo.
 
Per ogni secondo, la funzione deve stampare il tempo trascorso e l'altezza a cui si trova la palla in quel determinato secondo.
Ad esempio, se al tempo 0, la palla si trova ad altezza 0 cm, allora la funzione stamperà:
 
"Tempo: 0 Altezza: 0"
 
Se avviene il rimbalzo, la funzione deve stampare il tempo trascorso e la parola "Rimbalzo!".
Ad esempio, se il rimbalzo avviene al tempo 4, allora la funzione stamperà:
 
"Tempo: 4 Rimbalzo!"""


def rimbalzo():
    
    t = 0
    r = 0 
    
    while  r < 5:
        if t == 0:
            h = 0.0
            v = 100
            print(f"Tempo : {t}, altezza : {h}")
            t +=1
        
        if t !=0:
            h = h + v
            v = v - 96 
            if h > 0:
                print(f"Tempo : {t}, altezza : {h}")
                t += 1
        
            if h < 0:
                h = h * (-0.5)
                v = v * (-0.5)
                print(f"Tempo : {t}, Rimbalzo!")
                r +=1
                t +=1

"""Si immagini una funzione che comprime i file all'80% e li salva su un supporto di memorizzazione. Prima che il file compresso venga memorizzato, 
deve essere diviso in blocchi da 512 byte ciascuno.
 
Si sviluppi in Python un algoritmo per questa funzione che prende in input una lista di valori interi, dove ogni valore intero della lista rappresenta 
la dimensione non compressa di un singolo file espressa in byte.
 
Tale funzione deve utilizzare un ciclo per iterare la lista e, per ogni dimensione non compressa, deve calcolare la dimensione compressa di tale 
file espressa come float (ovvero deve calcolare l' 80% della dimensione non compressa), calcolare il numero di blocchi (arrotondato al numero intero più vicino) 
da 512 byte necessari per la memorizzazione, al fine di determinare se il file compresso può essere salvato nello spazio rimanente nel supporto di memorizzazione
 o meno.
 
In caso affermativo, il programma memorizza il file. In tal caso, la funzione deve stampare la dimensione originale del file, la dimensione compressa,
 i blocchi utilizzati per memorizzare il file in questione e i blocchi disponibili rimasti sul supporto di memorizzazione. 
Ad esempio, se è possibile salvare sul supporto di memorizzazione un file avente dimensione pari a 1100 byte, la funzione stamperà:
 
"File di 1100 byte compresso in 880.0 byte e memorizzato. Blocchi usati: 2. Blocchi rimanenti: 998."
 
Il ciclo continua finché non viene riscontrato un file della lista la cui dimensione compressa occupa un numero di blocchi più grande di quelli rimasti
 disponibili sul supporto di memorizzazione. In tal caso, la funzione deve avvisare l'utente che lo spazio disponibile sul supporto di memorizzazione non è 
 sufficiente per salvare il file. 
Ad esempio, se non è possibile salvare sul supporto di memorizzazione un file avente dimensione pari a 1048576 byte, la funzione stamperà:
 
"Non è possibile memorizzare il file di 1048576 byte. Spazio insufficiente."

Inizialmente, il numero totale di blocchi disponibili sul supporto di memorizzazione per il salvataggio dei file è un numero intero pari a 1000 blocchi. """

def memorizza_file(files: list[int]) -> None:
    spazio_totale_blocchi = 1000

    for file in files:
        new_file : float = file/100 * 80
        n = round(new_file / 512)
        if n < spazio_totale_blocchi:
            spazio_totale_blocchi -= n
            print(f"File di 1100 {file} compresso in {new_file} byte e memorizzato. Blocchi usati: {n}. Blocchi rimanenti: {spazio_totale_blocchi}.")
        else:
            print(f"Non è possibile memorizzare il file di {file}. Spazio insufficiente.")
        break

memorizza_file([1100, 20000, 1048576, 512, 5000])

memorizza_file([1100])

    


