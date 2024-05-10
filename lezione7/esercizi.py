#Scrivi una funzione che converte una temperatura da gradi Celsius a Fahrenheit e viceversa a seconda del parametro to_fahrenheit. 
#Utilizza il concetto di parametri opzionali per il parametro to_fahrenheit.

"""def to_fahrenheit(temperature : float, celsius = None) ->float:
    if celsius is False:
        temperature = (temperature - 32)*5/9
    else:
        temperature = ((temperature*9)/5) + 32
    return temperature

print(to_fahrenheit(32,False))"""

#Scrivi una funzione che determina se un numero è 'magico'. Un numero è considerato magico se è divisibile per 4 ma non per 6.

def numero_magico(num: int) -> bool:
    if num % 4 == 0 and  num % 6 != 0:
        return True
    else:
        return False

print(numero_magico(24))



###PARTE 1 Scrivi una funzione chiamata create_contact() che accetta il nome e cognome, e-mail (facoltativo) e numero di telefono (facoltativo).
# La funzione dovrebbe restituire un dizionario con i dettagli del contatto.

def create_contact(name: str, email: str=None, telefono: int=None) -> dict:
    
    contact : dict = { "name" : name,
                        "email" : email,
                        "telefono" : telefono}
    return contact

#PARTE 2
#Scrivi una funzione chiamata update_contact() che accetta il dizionario creato, il nome e cognome del contatto da aggiornare, e il dettaglio 
#facoltativo da aggiornare. Questa funzione dovrebbe aggiornare il dizionario del contatto.

def update_contact(contact: dict, name: str, email: str =None, telefono: int=None) -> dict:

    if contact["name"] == name:
        if email:
            contact["email"] = email

        if telefono:
            contact["telefono"] = telefono

    return contact

contact = create_contact("Mario Rossi", email="mario.rossi@gmail.com", telefono=788787)
print(create_contact("Mario Rossi", email="mario.rossi@gmail.com", telefono=788787))
print(update_contact(contact, "Mario Rossi", telefono=123456789))







#Scrivi una funzione che elimini dalla lista dati certi elementi specificati in un dizionario. Il dizionario contiene elementi da 
#rimuovere come chiavi e il numero di volte che devono essere rimossi come valori.