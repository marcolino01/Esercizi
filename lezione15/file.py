file = open("lezione15/prova.txt") 

try:
    pass                                  # INIZIA A LEGGERE RIGA PER RIGA IL FILE
finally:                                  #FINALLY FA IL COMANDO A PRESCINDER, QUINDI SE CRASHA IL TRY IL FINALLY LO CHIUDERA' SEMPRE
    file.close()

with open("lezione15/prova.txt") as file:         #WITH : TUTTO QUELLO CHE STA ALL'INTERNO DI WITH VIENE CHIUSO AUTOMATICAMENTE SEMPRE ANCHE IN CASO DI CRASH

    pass


class ContextManager:

    def __enter__(self):

        print("Risorsa acquisita")
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):

        if exc_type is not None:

            pass
        print("Risorsa rilasciata")
        return False
    
with ContextManager() as manager:

    print("sono dentro with")
