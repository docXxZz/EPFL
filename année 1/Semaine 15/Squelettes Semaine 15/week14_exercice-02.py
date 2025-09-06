from PIL import Image
import numpy as np

# A implémenter
def grayscale_contrast(numpy_image):
    """
    Ajuste le contraste d'une image en niveaux de gris.
    Étire les valeurs des pixels pour couvrir toute la plage de 0 à 255.
    """
    min_val = np.min(numpy_image)
    max_val = np.max(numpy_image)
    
    if max_val - min_val == 0:  # Évite la division par zéro
        return numpy_image
    
    contrasted = (numpy_image - min_val) * 255 / (max_val - min_val)
    return contrasted.astype(np.uint8)

# A implémenter
def color_contrast(numpy_image):
    """
    Ajuste le contraste d'une image couleur.
    Étire les valeurs des pixels pour chaque canal (R, G, B) indépendamment.
    """
    contrasted = np.zeros_like(numpy_image, dtype=np.float32)
    for channel in range(3):  # Parcourt les canaux R, G, B
        min_val = np.min(numpy_image[:, :, channel])
        max_val = np.max(numpy_image[:, :, channel])
        
        if max_val - min_val == 0:  # Évite la division par zéro
            contrasted[:, :, channel] = numpy_image[:, :, channel]
        else:
            contrasted[:, :, channel] = (numpy_image[:, :, channel] - min_val) * 255 / (max_val - min_val)
    
    return contrasted.astype(np.uint8)

# Code pour la visualisation, ne pas modifier ci-dessous
# Lecture des images
grayscale_image = np.array(Image.open('in/bridge.png').convert("L"))
color_image = np.array(Image.open('in/tree.jpg'))

# Modification du contraste
grayscale_contrasted = grayscale_contrast(grayscale_image)
color_contrasted = color_contrast(color_image)

# Sauvegarde des images
Image.fromarray(np.vstack([grayscale_image, grayscale_contrasted])).save('out/ex2_grayscale.jpg')
Image.fromarray(np.vstack([color_image, color_contrasted])).save('out/ex2_color.jpg')