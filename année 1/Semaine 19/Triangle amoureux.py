def has_love_triangle(n, loves):
    # On vérifie pour chaque avion s'il forme un triangle amoureux
    for i in range(n):
        a = loves[i] - 1  # L'avion que i aime
        b = loves[a] - 1  # L'avion que a aime
        c = loves[b] - 1  # L'avion que b aime
        
        # Vérifier si c revient à i, formant ainsi un triangle amoureux
        if c == i:
            return "YES"
    
    return "NO"

# Lecture de l'entrée
n = int(input())
loves = list(map(int, input().split()))

# Affichage du résultat
print(has_love_triangle(n, loves))
