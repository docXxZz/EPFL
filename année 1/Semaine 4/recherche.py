from PIL import Image
from collections import deque

def voisins_non_visites(image, noeud):
    x, y = noeud
    voisins = []
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Gauche, Droite, Haut, Bas
    
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < image.width and 0 <= ny < image.height:
            if image.getpixel((nx, ny)) == (255, 255, 255):  # On considère le blanc comme visitable
                voisins.append((nx, ny))
    
    return voisins

def noeud_depart(image):
    for y in range(image.height):
        for x in range(image.width):
            if image.getpixel((x, y)) == (255, 255, 255):  # Cherche le premier pixel blanc
                return (x, y)
    return None

def dessiner_chemin(image, chemin):
    for x, y in chemin:
        image.putpixel((x, y), (255, 0, 0))

def parcours_en_profondeur(image, depart):
    stack = [(depart, [depart])]  # Une pile qui contient le noeud courant et le chemin parcouru jusqu'à ce noeud
    visites = set()  # Ensemble des noeuds visités

    while stack:
        noeud, chemin = stack.pop()
        if noeud in visites:
            continue
        
        visites.add(noeud)
        
        # On vérifie si on est arrivé à la sortie (un pixel en bas à droite par exemple)
        if noeud == (image.width - 1, image.height - 1):  # Sortie en bas à droite
            return chemin
        
        for voisin in voisins_non_visites(image, noeud):
            if voisin not in visites:
                stack.append((voisin, chemin + [voisin]))
    
    return None  # Si aucun chemin n'est trouvé

def parcours_en_largeur(image, depart):
    queue = deque([(depart, [depart])])  # Une file pour la recherche en largeur
    visites = set()  # Ensemble des noeuds visités

    while queue:
        noeud, chemin = queue.popleft()
        if noeud in visites:
            continue
        
        visites.add(noeud)
        
        if noeud == (image.width - 1, image.height - 1):  # Sortie en bas à droite
            return chemin
        
        for voisin in voisins_non_visites(image, noeud):
            if voisin not in visites:
                queue.append((voisin, chemin + [voisin]))
    
    return None

if __name__ == "__main__":
    # Nom du fichier à ouvrir
    nom = "labyrinthe.png"

    # Nom complet du fichier à ouvrir
    from pathlib import Path
    nom_complet = Path(__file__).with_name("labyrinthe.png")
    
    # Ouverture de l'image
    image = Image.open(nom_complet)

    # Recherche du chemin
    chemin = parcours_en_profondeur(image, noeud_depart(image))
    dessiner_chemin(image, chemin)

    # Nom du fichier de résultat
    nom_resultat = nom[:-4] + "_resultat.png"

    # Nom complet du fichier de résultat
    nom_complet_resultat = Path(__file__).with_name(nom_resultat)

    # Sauvegarde du résultat
    image.resize((image.width * 5, image.height * 5), Image.Resampling.BOX).save("labyrinthe.search.png")