import numpy as np
from PIL import Image

# A implémenter
def encode_images(image_1, image_2, one_time_pad):
    return image_1, image_2, one_time_pad

# A implémenter
def generate_one_time_pad(shape):
    return np.zeros(shape, dtype=np.uint8)


# Code pour la visualisation, ne pas modifier ci-dessous
# Lecture des images
epfl = np.array(Image.open('in/EPFL.jpg'))
cervin = np.array(Image.open('in/CERVIN.jpg'))

# Génération des images encodées et attaque
assert epfl.shape == cervin.shape
one_tip_pad = generate_one_time_pad(epfl.shape)
epfl_encoded, cervin_encoded, otp_attack = encode_images(epfl, cervin, one_tip_pad)

# Sauvegarde des images
first_line = np.hstack((epfl, cervin, one_tip_pad))
second_line = np.hstack((epfl_encoded, cervin_encoded, otp_attack))
Image.fromarray(np.vstack([first_line, second_line]).astype(np.uint8)).save('out/ex3_xor-otp.png')