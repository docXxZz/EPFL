from PIL import Image, ImageDraw
from queue import PriorityQueue

def a_star(graph, depart, arrivee):
    # File de priorité pour le traitement des nœuds
    file_noeuds = PriorityQueue()
    file_noeuds.put((0, depart))

    origines = {}  # Origine de chaque nœud atteint
    origines[depart] = None
    distances = {}  # Distances des nœuds atteints depuis le départ
    distances[depart] = 0

    while not file_noeuds.empty():
        # Récupération du prochain nœud
        _, noeud = file_noeuds.get()

        # Vérification de si on a atteint l'arrivée
        if noeud == arrivee:
            chemin = []
            while noeud is not None:
                chemin.append(noeud)
                noeud = origines[noeud]
            chemin.reverse()
            return chemin

        # Ajout des voisins s'ils sont plus rapidement atteignables
        for voisin in voisins(graph, noeud):
            # Calcul de la distance du voisin au départ
            d = distances[noeud] + distance(graph, noeud, voisin)
            if voisin not in distances or d < distances[voisin]:
                distances[voisin] = d
                origines[voisin] = noeud
                priorite = d + estimation(graph, voisin, arrivee)
                file_noeuds.put((priorite, voisin))

    return None  # Aucun chemin trouvé

def voisins(graph, noeud):
    """
    Retourne les voisins du noeud dans le graphe.
    Pour une image, cela pourrait être les pixels adjacents (haut, bas, gauche, droite).
    """
    voisins = []
    x, y = noeud
    rows, cols = len(graph), len(graph[0])

    # Directions: gauche, droite, haut, bas
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < rows and 0 <= ny < cols and graph[nx][ny] == 0:  # 0 = libre, 1 = obstacle
            voisins.append((nx, ny))

    return voisins

def distance(graph, noeud, voisin):
    """
    Calcule la distance entre deux nœuds. Ici on utilise une distance de 1
    pour les mouvements vers les voisins directs (gauche, droite, haut, bas).
    """
    return 1

def estimation(graph, noeud, arrivee):
    """
    Estimation heuristique de la distance entre le nœud actuel et le nœud d'arrivée.
    On peut utiliser la distance de Manhattan dans un espace 2D.
    """
    x1, y1 = noeud
    x2, y2 = arrivee
    return abs(x1 - x2) + abs(y1 - y2)  # Distance de Manhattan

def image_to_grid(image_path):
    """
    Convertit une image en niveaux de gris en une grille (0 pour navigable, 1 pour obstacle).
    """
    image = Image.open(image_path).convert("L")  # Convertit en niveaux de gris
    grid = []
    width, height = image.size

    for y in range(height):
        row = []
        for x in range(width):
            pixel_value = image.getpixel((x,y))
            
            if pixel_value != (0, 0, 0):  # Si le pixel est noir, il n'est pas navigable
                row.append(1)
            else:
                row.append(0)  # Sinon, c'est navigable
        grid.append(row)

    return grid, image

def draw_path_on_image(image, path):
    """
    Dessine le chemin sur l'image en rouge.
    """
    draw = ImageDraw.Draw(image)
    for position in path:
        draw.point(position, fill=(255, 0, 0))  # Dessine en rouge
    return image

# Exemple d'utilisation
if __name__ == "__main__":
    image_path = "/Users/macbook/Library/Mobile Documents/com~apple~CloudDocs/EPFL/Code/Semaine 5/carte-1.png"  # Remplacez par le chemin de votre image
    start = (18, 50)  # Coordonnées de départ (à ajuster selon votre image)
    end = (52, 9)    # Coordonnées d'arrivée (à ajuster selon votre image)

    # Convertir l'image en une grille
    grid, image = image_to_grid(image_path)

    # Appliquer l'algorithme A*
    path = a_star(grid, start, end)

    if path:
        print("Chemin trouvé :", path)
        # Dessiner le chemin sur l'image
        result_image = draw_path_on_image(image, path) 
        result_image.show()  # Afficher l'image avec le chemin dessiné
    else:
        print("Aucun chemin trouvé")