def compter_lacs(n, m, carte):
    # Crée une matrice pour suivre les cases visitées
    visite = [[False] * m for _ in range(n)]

    # Fonctions pour se déplacer vers les 4 directions adjacentes (haut, bas, gauche, droite)
    def voisins(x, y):
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and not visite[nx][ny] and carte[nx][ny] == 'O':
                yield nx, ny

    # Fonction DFS pour marquer un lac
    def marquer_lac(x, y):
        stack = [(x, y)]
        visite[x][y] = True
        while stack:
            cx, cy = stack.pop()
            for nx, ny in voisins(cx, cy):
                visite[nx][ny] = True
                stack.append((nx, ny))

    # Parcourt la carte pour trouver des lacs
    nombre_de_lacs = 0
    for i in range(n):
        for j in range(m):
            if carte[i][j] == 'O' and not visite[i][j]:
                # Nous avons trouvé un nouveau lac, lancer DFS
                marquer_lac(i, j)
                nombre_de_lacs += 1

    return nombre_de_lacs

# ---- Demander les dimensions et la carte à l'utilisateur ----
# Entrer les dimensions de la carte
n = int(input("Entrez la hauteur de la carte : "))
m = int(input("Entrez la largeur de la carte : "))

# Entrer les lignes de la carte
carte = []
print("Entrez les lignes de la carte :")
for _ in range(n):
    ligne = input().strip()  # Suppression des espaces inutiles
    while len(ligne) != m:
        print(f"La ligne doit contenir exactement {m} caractères.")
        ligne = input().strip()
    carte.append(ligne)

# Appel de la fonction avec la carte définie par l'utilisateur
print("Nombre de lacs :", compter_lacs(n, m, carte))