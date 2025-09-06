import numpy as np
from PIL import Image

# A implémenter
def naive_grayscale(numpy_image):
    """
    Conversion naïve en niveaux de gris : calcul de la moyenne des canaux R, G, B.
    """
    numpy_image = numpy_image.astype(np.int32)  # Attention à l'overflow en uint8
    grayscale = np.mean(numpy_image, axis=2)
    return grayscale.astype(np.uint8)

# A implémenter
def ntsc_grayscale(numpy_image):
    """
    Conversion NTSC en niveaux de gris : pondération des canaux selon les standards NTSC.
    Pondération : 0.2989 * R + 0.5870 * G + 0.1140 * B.
    """
    numpy_image = numpy_image.astype(np.int32)  # Attention à l'overflow en uint8
    grayscale = (0.2989 * numpy_image[:, :, 0] +
                 0.5870 * numpy_image[:, :, 1] +
                 0.1140 * numpy_image[:, :, 2])
    return grayscale.astype(np.uint8)

# A implémenter
def red_grayscale(numpy_image):
    """
    Conversion en niveaux de gris basée uniquement sur le canal rouge.
    """
    grayscale = numpy_image[:, :, 0]
    return grayscale.astype(np.uint8)

# A implémenter
def green_grayscale(numpy_image):
    """
    Conversion en niveaux de gris basée uniquement sur le canal vert.
    """
    grayscale = numpy_image[:, :, 1]
    return grayscale.astype(np.uint8)

# A implémenter
def blue_grayscale(numpy_image):
    """
    Conversion en niveaux de gris basée uniquement sur le canal bleu.
    """
    grayscale = numpy_image[:, :, 2]
    return grayscale.astype(np.uint8)

# Code pour la visualisation, ne pas modifier ci-dessous
# Lecture de l'image
np_image = np.array(Image.open('in/starry.jpg'))

# Conversions en niveaux de gris
naive_gs = naive_grayscale(np_image)
ntsc_gs = ntsc_grayscale(np_image)
red_gs = red_grayscale(np_image)
green_gs = green_grayscale(np_image)
blue_gs = blue_grayscale(np_image)

# Sauvegarde de l'image
first_line = np.hstack([np_image,
                        np.repeat(naive_gs[:, :, np.newaxis], 3, axis=2),
                        np.repeat(ntsc_gs[:, :, np.newaxis], 3, axis=2)]
                       )
second_line = np.hstack([np.repeat(red_gs[:, :, np.newaxis], 3, axis=2),
                         np.repeat(green_gs[:, :, np.newaxis], 3, axis=2),
                         np.repeat(blue_gs[:, :, np.newaxis], 3, axis=2)])
Image.fromarray(np.vstack([first_line, second_line])).save('out/ex1_grayscales.jpg')