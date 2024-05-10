
def aggrega_voti(voti: list[dict]) -> dict[str:list[int]]:
    voti_aggregati : dict = {}
    
    for i in voti:
        studente = i["nome"]
        voto = i["voto"]
        if studente in voti_aggregati:
            voti_aggregati[studente].append(voto)
        else:
            voti_aggregati[studente] = [voto]
    return voti_aggregati

print(aggrega_voti([{'nome': 'Alice', 'voto': 90}, {'nome': 'Bob', 'voto': 75}, {'nome': 'Alice', 'voto': 85}]))