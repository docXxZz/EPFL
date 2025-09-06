def min_groups(n, managers):
    from collections import defaultdict, deque

    tree = defaultdict(list)  # Graphe sous forme d'arbre
    roots = []  # Liste des employés sans supérieur immédiat

    # Construire la hiérarchie
    for i in range(n):
        if managers[i] == -1:
            roots.append(i)  # Pas de supérieur immédiat => c'est une racine
        else:
            tree[managers[i] - 1].append(i)  # Ajouter l'employé à son supérieur

    # Fonction pour trouver la profondeur maximale d'un arbre avec BFS
    def bfs(root):
        queue = deque([(root, 1)])  # (employé, profondeur actuelle)
        max_depth = 1
        while queue:
            node, depth = queue.popleft()
            max_depth = max(max_depth, depth)
            for child in tree[node]:
                queue.append((child, depth + 1))
        return max_depth

    # Trouver la profondeur maximale parmi tous les arbres
    max_groups = max(bfs(root) for root in roots)
    
    return max_groups

# Lecture de l'entrée
n = int(input())
managers = [int(input()) for _ in range(n)]
map(int, input().split())
# Affichage du résultat
print(min_groups(n, managers))