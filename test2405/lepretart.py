import random
t : int = 0
h : int = 0

def positions(t, h):
    lista = []
    for i in range (1, 71):
        lista.append(f"{i} - ")
    if t < 71:
        lista[t] = "T"  
    else :
        lista[t] = 70
    if h < 71:
        lista[h] = "H"
    else :
        lista[h] = 70
    if t == h:
        print("OUCH!!!")

    dangers = {lista[15]: -3, lista[30]: -5, lista[45]: -7}
    bonus = {lista[10]: 5, lista[25]: 3, lista[50]: 10}

    for key,value in dangers.items():
        if lista[h] in dangers:
            h += value
            lista[h] = "H"
        if lista[t] in dangers:
            t += value
            lista[t] = "T"
        
    for key,value in bonus.items():
        if lista[h] in bonus:
            h += value
            lista[h] = "H"
        if lista[t] in bonus:
            t += value
            lista[t] = "T"

    print(lista)


    
    
def hare(h):
    move = random.randint(1, 10)
    stamina = 100

    if h < 70:
        if 1 <= move <= 2:
            print("LEPRE RIPOSA!AVANZA DI 0 CASELLE!")
            h += 0
            if stamina <= 90:
                stamina += 10
            else:
                stamina = 100
            return h
        elif 3 <= move <= 4:
            if stamina - 15 > 0:
                print("GRANDE BALZO!!!LA LEPRE AVANZA DI 9 QUADRATI!!")
                h += 9
                return h
            else:
                stamina += 10
        elif move == 5:
            if stamina - 20 > 0:
                print("GRANDE SCIVOLATA!!LA LEPRE ARRETRA DI 12 QUADRATI!!")
                if h > 12:
                    h -= 12
                    return h
                else:
                    h = 0
                    return h
            else:
                stamina += 10
        elif 6 <= move <= 8:
            if stamina - 5 > 0:
                print("PICCOLO BALZO!!LA LEPRE AVANZA DI 1 QUADRATO")
                h += 1
                return h
            else:
                stamina += 10
        else:
            if stamina - 8 > 0:
                print("PICCOLA SCIVOLATA!!LA LEPRE ARRETRA DI 2 QUADRATI")
                if h > 2:
                    h -= 2
                    return h
                else:
                    h = 0
                    return h
            else:
                stamina += 10
    else:
        h = 70
        return h

def tortoise(t):
    move = random.randint(1, 10)
    stamina = 100

    if t < 70:
        if 1 <= move <= 5:
            if stamina - 5 > 0:
                print("PASSO VELOCE!!LA TARTARUGA AVANZA DI 3 QUADRATI")
                t += 3
                return t
            else:
                stamina += 10
        elif 6 <= move <= 7:
            print("SCIVOLATA!!LA TARTARUGA ARRETRA DI 6 QUADRATI")    #NON DEVE ANDARE SOTTO 1
            if t > 6:
                if stamina - 10 > 0:
                    t -=6
                    return t
                else:
                    stamina += 10
            else:
                t = 0
                return t
        else:
            if stamina - 3 > 0:
                print("PASSO LENTO!!!LA TARTARUGA AVANZA DI 1 QUADRATO")
                t +=1
                return t
            else:
                stamina += 10
    else:
        t = 70
        return h

print("BANG !!!!! AND THEY'RE OFF !!!!!")   
while t < 71 or h < 71:

    positions(t,h)
    
    t = tortoise(t)
    h = hare(h)
    if t == 70:
        print("TORTOISE WINS! || VAY!!!")
        break
    if h == 70:
        print("HARE WINS || YUCH!!!")
        break
    


    