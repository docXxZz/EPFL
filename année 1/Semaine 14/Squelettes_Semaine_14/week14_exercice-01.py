import numpy as np
from PIL import Image

# Fonction pour convertir une image en niveaux de gris en gardant uniquement la composante rouge
def red_grayscale(image):
    return image[:, :, 0]

# Fonction pour convertir une image en niveaux de gris en gardant uniquement la composante verte
def green_grayscale(image):
    return image[:, :, 1]

# Fonction pour convertir une image en niveaux de gris en gardant uniquement la composante bleue
def blue_grayscale(image):
    return image[:, :, 2]

# Fonction pour convertir une image en niveaux de gris en utilisant la moyenne des composantes
def naive_grayscale(image):
    return np.mean(image, axis=2).astype(np.uint8)

# Fonction pour convertir une image en niveaux de gris en utilisant la formule NTSC
def ntsc_grayscale(image):
    return (image[:, :, 0] * 0.299 + image[:, :, 1] * 0.587 + image[:, :, 2] * 0.114).astype(np.uint8)

# Exemple d'utilisation avec une image RGB
def main():
    # Charger une image avec Pillow
    img = Image.open("./Semaine_14/Squelettes_Semaine_14/in/bridge.png")
    
    # Convertir en tableau NumPy
    img_array = np.array(img)

    # Appliquer les transformations
    red_img = red_grayscale(img_array)
    green_img = green_grayscale(img_array)
    blue_img = blue_grayscale(img_array)
    naive_img = naive_grayscale(img_array)
    ntsc_img = ntsc_grayscale(img_array)

    # Sauvegarder les images résultantes
    Image.fromarray(red_img).save("red_grayscale.jpg")
    Image.fromarray(green_img).save("green_grayscale.jpg")
    Image.fromarray(blue_img).save("blue_grayscale.jpg")
    Image.fromarray(naive_img).save("naive_grayscale.jpg")
    Image.fromarray(ntsc_img).save("ntsc_grayscale.jpg")

if __name__ == "__main__":
    main()