from PIL import Image
from random import randint, choice


def pieces_adjacentes_non_connectees(image, x, y):
    pieces = []
    for px, py in ((x + 2, y), (x - 2, y), (x, y + 2), (x, y - 2)):
        if 0 <= px < image.width and 0 <= py < image.height:
            if image.getpixel((px, py)) == (128, 128, 128):
                pieces.append((px, py))
    return pieces


def creer_labyrinthe(largeur, hauteur):
    if largeur % 2 != 1 or hauteur % 2 != 1:
        raise ValueError("Les dimensions doivent être impaires.")
    
    # Création de l'image
    image = Image.new("RGB", (largeur, hauteur), (0, 0, 0))

    for i in range(1, largeur, 2):
        for j in range(1, hauteur, 2):
            image.putpixel((i, j), (128, 128, 128))

    # On choisit une pièce au hasard
    x_courant = randint(0, largeur // 2 - 1) * 2 + 1
    y_courant = randint(0, hauteur // 2 - 1) * 2 + 1

    # On connecte la pièce
    image.putpixel((x_courant, y_courant), (255, 255, 255))

    # On crée un chemin depuis cette pièce
    chemin = []

    while True:

        # On récupère les pièces voisines non connectées
        voisins = pieces_adjacentes_non_connectees(image, x_courant, y_courant)
        if len(voisins) == 0:
            # On a atteint un cul-de-sac

            if len(chemin) == 0:
                # Si on est revenu au début, on a fini
                break

            # On revient en arrière
            x_courant, y_courant = chemin.pop()
            continue

        # On choisit une pièce voisine au hasard
        x_voisin, y_voisin = choice(voisins)

        # On connecte la pièce voisine
        image.putpixel((x_voisin, y_voisin), (255, 255, 255))

        # On supprime le mur entre les deux pièces
        image.putpixel((((x_courant + x_voisin) // 2), ((y_courant + y_voisin) // 2)), (255, 255, 255))

        # On ajoute la pièce courante au chemin
        chemin.append((x_courant, y_courant))

        # On passe à la pièce voisine
        x_courant, y_courant = x_voisin, y_voisin

    # On ajoute une entrée et une sortie
    x_debut, y_debut = randint(0, largeur // 2 - 1) * 2 + 1, 0
    x_fin, y_fin = randint(0, largeur // 2 - 1) * 2 + 1, hauteur - 1
    image.putpixel((x_debut, y_debut), (255, 255, 255))
    image.putpixel((x_fin, y_fin), (255, 255, 255))

    # On retourne l'image
    return image

if __name__ == "__main__":
    print("Bienvenue dans le générateur de labyrinthe !")
    print("Entrez les dimensions du labyrinthe (impaires).")
    while True:
        try:
            # On demande les dimensions
            largeur = int(input("Largeur : "))
            hauteur = int(input("Hauteur : "))

            # On vérifie que les dimensions sont impaires
            if largeur % 2 != 1 or hauteur % 2 != 1:
                print("Les dimensions doivent être impaires.")
            else:
                break
        except ValueError:
            # Si les dimensions ne sont pas des nombres entiers
            print("Les dimensions doivent être des nombres entiers impairs.")
    
    # On crée le labyrinthe
    image = creer_labyrinthe(largeur, hauteur)

    # On l'affiche
    image.show()
    image.save("labyrinthe.pro.png")
