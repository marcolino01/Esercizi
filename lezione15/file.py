file = open("lezione15/prova.txt") 


try:
    print("sono nella try")  
    file.readline()
    raise Exception("eccezione")
except Exception:
    print("sono nella except")                             
finally:     
    print(file)
    file.close()                         
    print("sono nella finally")

         
"""try:
    pass                                  # INIZIA A LEGGERE RIGA PER RIGA IL FILE
finally:                                  #FINALLY FA IL COMANDO A PRESCINDER, QUINDI SE CRASHA IL TRY IL FINALLY LO CHIUDERA' SEMPRE
    file.close()

with open("lezione15/prova.txt") as file:         #WITH : TUTTO QUELLO CHE STA ALL'INTERNO DI WITH VIENE CHIUSO AUTOMATICAMENTE SEMPRE ANCHE IN CASO DI CRASH
    line = file.readline()
    while line != '':                             #legge il file fino alla fine 
        print(line, end= '')
        line = file.readline()


with open("lezione15/prova.txt", "a") as file:         #con file.writelines() posso aggiungere liste di stringhe se aggiungo 'a' al posto di 'w' appende la lista di stringhe
    l = [f"ciao luca\n", f"ciao carlo\n"]
    file.writelines(l)"""

try:
    print("sono nel try")
    raise ValueError()
except Exception:
    print("sono nell?except")
else: 
    print("sono nell'else")
finally:
    print("sono nel finally")
"""class ContextManager:

    def __enter__(self):

        print("Risorsa acquisita")
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):

        if exc_type is not None:

            print("Eccezione")
        return False
    
try:  
    with ContextManager() as manager:

        print("ciao")
        print(manager)
except Exception:

    print()"""





