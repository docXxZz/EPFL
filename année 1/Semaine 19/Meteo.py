def peut_atteindre_alice(n, s, voie1, voie2):
    s -= 1  # Convertir en index 0-based
    
    # Si Bob ne peut pas partir de sa station sur la première voie, il ne peut pas aller plus loin
    if voie1[0] == 0:
        return "NO"

    # Si la station d'Alice est accessible directement sur la première voie
    if voie1[s] == 1:
        return "YES"

    # Vérifier s'il peut atteindre une station commune entre les deux voies après s
    for i in range(s, n):
        if voie1[i] == 1 and voie2[i] == 1:
            # Vérifier si on peut revenir à la station d'Alice via la deuxième voie
            if voie2[s] == 1:
                return "YES"
    
    return "NO"

# Lecture de l'entrée
n, s = map(int, input().split())
voie1 = list(map(int, input().split()))
voie2 = list(map(int, input().split()))

# Affichage du résultat
print(peut_atteindre_alice(n, s, voie1, voie2))