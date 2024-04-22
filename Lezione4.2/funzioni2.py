from tomlkit import key


def subtract_all(x:list[float], y:float) -> list[float]:
    # x = [1,2,3,4,5]
    # y = [-4,-3,-2,-1,0]
    xylist: list[float] = []
    for i in x:
        z : float = i - y
        xylist.append(z)
        
    return xylist



mylist : list[float] = [1,2,3,4,5]
y : float = 10 
result = subtract_all(mylist, y)
print(result)



def subtract_list(x:list[float], y:list[float]) -> list[float]:
    res : list[float] = []
    if len(x) >= len(y):
        for i in range(len(y)):                                           #|visto che abbiamo due for in comune che fanno la stessa cosa possiamo creare una
            diff : float = x[i]-y[i]                                      #|funzione per il for   def add_diff_to_res(res:list[float],x:list[float], y:list[float], lenght:int)
            res.append(diff)                                              #                        dove ci metto il ciclo for che abbiamo creato
    else:                                                                  
        for i in range(len(x)):
            diff : float = x[i]-y[i]
            res.append(diff)
    return res

lista1 : list[float] = [1,2,3,4,5]
lista2 : list[float] = [-2,3,1,-2,3]
differenza_liste = subtract_list(lista1,lista2)
print(differenza_liste)





s: str = "La meccanica quantistica è la teoria fisica che descrive il comportamento della materia, della radiazione e le reciproche interazioni, con particolare riguardo ai fenomeni caratteristici della scala di lunghezza o di energia atomica e subatomica, dove le precedenti teorie classiche risultano inadeguate. Come caratteristica fondamentale, la meccanica quantistica descrive la radiazione e la materia sia come fenomeni ondulatori che come entità particellari, al contrario della meccanica classica, che descrive la luce solamente come un'onda e, ad esempio, l'elettrone solo come una particella. Questa inaspettata e controintuitiva proprietà della realtà fisica, chiamata dualismo onda-particella, è la principale ragione del fallimento delle teorie sviluppate fino al XIX secolo nella descrizione degli atomi e delle molecole. La relazione tra natura ondulatoria e corpuscolare è enunciata nel principio di complementarità e formalizzata nel principio di indeterminazione di Heisenberg. Esistono numerosi formalismi matematici equivalenti della teoria, come la meccanica ondulatoria e la meccanica delle matrici; al contrario, ne esistono numerose e discordanti interpretazioni riguardo all'essenza ultima del cosmo e della natura, che hanno dato vita a un dibattito tuttora aperto nell'ambito della filosofia della scienza. La meccanica quantistica rappresenta, assieme alla teoria della relatività, uno spartiacque rispetto alla fisica classica, portando alla nascita della fisica moderna. Attraverso la teoria quantistica dei campi, generalizzazione della formulazione originale che include il principio di relatività ristretta, essa è a fondamento di molte altre branche della fisica, come la fisica atomica, la fisica della materia condensata, la fisica nucleare, la fisica delle particelle, la chimica quantistica."
def counter(s: str) -> list[int]:
    """la lista deve contenere numero di caratteri,numero di parole,numero di parole distinte,numero di frasi"""
    numbers: list[float] = []
    numbers.append(len(s))
    numbers.append(len(s.split()))
    numbers.append(len(s.split(".")) - 1)
    parole = s.split()
    parole_distinte = set(parole)
    numbers.append(len(parole_distinte))

    return numbers
print(counter(s))


def word_count(s: str) -> dict[str,int]:
     s = s.replace(".", "").replace(",","").replace(";","").replace("!","")
     parole : list[str] = s.split()
     diz : dict[str, int] = {}
     for i in parole:
         if i not in diz:
             diz[i] = 1
         else:
             diz[i] +=1
     return diz
print(word_count(s))


#filtro per le parole con compaiono piu di una volta
def word_count2(diz: dict) -> dict[str,int]:
    diz2 : dict[str, int] = {}
    for i in diz:
        if diz[i]!=1:
            diz2[i] = diz[i]
    return diz2
 
print(word_count2(word_count(s)))


     