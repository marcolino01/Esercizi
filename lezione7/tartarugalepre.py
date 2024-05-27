import random
t : int = 0
h : int = 0

def positions(t, h):
    lista = []
    for i in range (1, 71):
        lista.append(f"{i} - ")
    if t < 70 or h < 70:
        lista[t] = "T"  
        lista[h] = "H"
    else :
        lista[t] = 70
        lista[h] = 70
    if lista[t] == lista[h]:
        print("OUCH!!!")
    print(lista)


    
    
def hare(h):
    move = random.randint(1, 10)

    if h < 70:
        if 1 <= move <= 2:
            print("LEPRE RIPOSA!AVANZA DI 0 CASELLE!")
            h += 0
            return h
        elif 3 <= move <= 4:
            print("GRANDE BALZO!!!LA LEPRE AVANZA DI 9 QUADRATI!!")
            h += 9
            return h
        elif move == 5:
            print("GRANDE SCIVOLATA!!LA LEPRE ARRETRA DI 12 QUADRATI!!")
            if h > 12:
                h -= 12
                return h
            else:
                h = 1
                return h
        elif 6 <= move <= 8:
            print("PICCOLO BALZO!!LA LEPRE AVANZA DI 1 QUADRATO")
            h += 1
            return h
        else:
            print("PICCOLA SCIVOLATA!!LA LEPRE ARRETRA DI 2 QUADRATI")
            if h > 2:
                h -= 2
                return h
            else:
                h = 1
                return h
    else:
        h = 70
        return h

def tortoise(t):
    move = random.randint(1, 10)

    if t < 70:
        if 1 <= move <= 5:
            print("PASSO VELOCE!!LA TARTARUGA AVANZA DI 3 QUADRATI")
            t += t
            return h
        elif 6 <= move <= 7:
            print("SCIVOLATA!!LA TARTARUGA ARRETRA DI 6 QUADRATI")    #NON DEVE ANDARE SOTTO 1
            if t > 6:
                t -=6
                return t
            else:
                t = 1
                return t
        else:
            print("PASSO LENTO!!!LA TARTARUGA AVANZA DI 1 QUADRATO")
            t +=1
            return t
    else:
        t = 70
        return h

    
while t < 70 or h < 70:

    positions(t,h)
    
    t = tortoise(t)
    h = hare(h)



