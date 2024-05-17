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