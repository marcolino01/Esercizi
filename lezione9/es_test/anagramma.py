def anagram(s: str, t: str) -> bool:
    diz_s : dict = {}
    diz_t : dict = {}
    if len(s) != len(t):
        return False
    else:
        for i in s:
            if i in diz_s:
                diz_s[i] += 1
            else: 
                diz_s[i]= 1
        for i in t:
            if i in diz_t:
                diz_t[i] +=1
            else:
                diz_t[i] =1
    
    if diz_s == diz_t:
        return True
            
print(anagram("roma","amor"))


"""s = list(s.lower())
t = list(t.lower())
return sorted(s) == sorted(t)"""


"""if len(s) == len(t)
        char_s: dict[str, int] = {s[i]: 0 for i in range (len(s))}
        for elem in s:
            char_s[elem] +=1
            
        for elem in t:
            if elem in char_s.keys()
                char_s[elem] -=1
            else:
                return False
        return sum(list(char_s.values())) == 0
    else:
        return False"""