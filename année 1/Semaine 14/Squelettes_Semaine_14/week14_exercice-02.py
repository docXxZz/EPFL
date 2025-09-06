from PIL import Image
import numpy as np

# A implémenter
def grayscale_contrast(numpy_image):
    numpy_image = numpy_image.astype(np.int32)
    return numpy_image.astype(np.uint8)

# A implémenter
def color_contrast(numpy_image):
    numpy_image = numpy_image.astype(np.int32)
    return numpy_image.astype(np.uint8)

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