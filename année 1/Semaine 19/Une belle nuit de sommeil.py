def est_une_etoile(n, m, edges):
    if m != n - 1:  # Un graphe étoile doit avoir exactement n-1 arêtes
        return "CAUCHEMAR"

    degree = [0] * n  # Liste pour stocker le degré de chaque sommet

    for a, b in edges:
        degree[a] += 1
        degree[b] += 1

    # Un graphe étoile doit avoir un centre avec n-1 connexions et tous les autres sommets avec 1 connexion
    center_count = 0
    leaf_count = 0

    for d in degree:
        if d == n - 1:
            center_count += 1
        elif d == 1:
            leaf_count += 1
        elif d > 1:
            return "CAUCHEMAR"

    if center_count == 1 and leaf_count == n - 1:
        return "REPOS"
    else:
        return "CAUCHEMAR"

# Lecture de l'entrée
n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# Affichage du résultat
print(est_une_etoile(n, m, edges))