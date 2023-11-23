L = [8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91]

def trie(liste):
    r=[]
    while liste:
        mini=min(liste)
        liste.remove(mini)
        r.append(mini)
    return r
     
print(trie(L))