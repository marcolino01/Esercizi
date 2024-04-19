from optparse import Values


def area_rettangolo(x: float, y: float) -> float:
    area = x*y
    return area

x, y= 2, 3
out: float = area_rettangolo(x,y)
print(f"L'area del rettangolo con x={x} e y={y} è {out}")


#################################################
#questa funzione prende in input un dizionario (e.s. d = {"ciao": 2, "hello": 3}) e restituisce un nuovo dizionario fatto così
#d1 = {"ciao": 2/5,"hello" : 3/5} dove 5 è la somma deivalori di d, ossia 2 e 5


def rewrite_dict(d : dict[str, int]) -> dict[str, int]:
        print(f"il dizionario di input è {d}")
        somma: float= sum(list(d.values()))
        print(f"la somma è {somma}")
        out : dict[str,int] ={}
        for key in d:
              out[key] = d[key]/somma
        return out

d = {"ciao":2 ,"hello":3}
output= rewrite_dict(d)
print(f"il nuovo output è {output}")




##funzione sottrazione


def subtract(x:float, y:float)  ->float:
      sottrazione: float= x-y
      return sottrazione


x, y = float(input("inserisci il primo numero:")), float(input("inserisci il secondo numero:"))
print(f"la differenza tra {x} e {y} è {subtract(x,y)}")


#######################funzione che prende in input una lista di numeri reali e restituisce la madiana

def median(l: list[float]) ->float:
      l.sort()
      mid = len(l)//2
      if len(l)%2==1:
            mediana = l[mid]
      else :
           mediana = (l[mid]+l[mid - 1])/2
      return mediana

lista_input : str = input("inserisci i numeri della lista: ")                #per creare una lista input devo converire la stringa in una lista float
l : list[str] = lista_input.split()
l1 : list[float] = []
for i in l:
      l1.append(float(i))
print(median(l1))



#######funzione per differenza comulativa

def diff_cum(l3: list[float]) -> float:
      diff : float =l3[0]
      for i in l3[1:]:
            diff-= i
      return diff

lista_input : str = input("inserisci i numeri della lista: ")                
l4 : list[str] = lista_input.split()
l5 : list[float] = []
for i in l4:
      l5.append(float(i))
print(diff_cum(l5))


      
