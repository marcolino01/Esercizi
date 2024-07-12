import string
def sposta_caratter(c: str, chiave : int):
        lettere : str = string.ascii_lowercase
        numeri = range(1, len(lettere) + 1)
        diz : dict[str, int] = dict(zip(lettere, numeri))
        if c in diz.keys():
            chiave += diz[c]
            n = chiave
            for k,v in diz.items():
                if n == v:
                    return k
                
def codifica(testoInChiaro: str):
        for i in testoInChiaro:
            risultato : str = ""
            sposta_caratter(i, 3)
            risultato += i
        return risultato
                     
            
print(codifica("abcdef"))
