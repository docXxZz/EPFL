def meilleur_coup(n):
    if n<=4:
        return n
    else:
        for i in(1, 2, 3, 4):
            if meilleur_coup(n-i) is None:
                return i
        return None
    
    
print (meilleur_coup(17))

for i in range(16):
    print(i, "-->", meilleur_coup(i))