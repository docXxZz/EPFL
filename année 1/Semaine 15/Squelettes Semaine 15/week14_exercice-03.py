import numpy as np
from PIL import Image

# A implémenter
def encode_images(image_1, image_2, one_time_pad):
    """
    Chiffre deux images en utilisant un masque à usage unique (One-Time Pad).
    Retourne également l'attaque XOR entre les deux images encodées.
    """
    # Chiffrement des images en utilisant XOR
    image_1_encoded = np.bitwise_xor(image_1, one_time_pad)
    image_2_encoded = np.bitwise_xor(image_2, one_time_pad)
    
    # Attaque : XOR des deux images encodées
    otp_attack = np.bitwise_xor(image_1_encoded, image_2_encoded)
    
    return image_1_encoded, image_2_encoded, otp_attack

# A implémenter
def generate_one_time_pad(shape):
    """
    Génère un masque à usage unique (One-Time Pad) de la même taille que l'image.
    Les valeurs sont aléatoires dans l'intervalle [0, 255].
    """
    return np.random.randint(0, 256, size=shape, dtype=np.uint8)

# Code pour la visualisation, ne pas modifier ci-dessous
# Lecture des images
epfl = np.array(Image.open('in/EPFL.jpg'))
cervin = np.array(Image.open('in/CERVIN.jpg'))

# Génération des images encodées et attaque
assert epfl.shape == cervin.shape
one_time_pad = generate_one_time_pad(epfl.shape)
epfl_encoded, cervin_encoded, otp_attack = encode_images(epfl, cervin, one_time_pad)

# Sauvegarde des images
first_line = np.hstack((epfl, cervin, one_time_pad))
second_line = np.hstack((epfl_encoded, cervin_encoded, otp_attack))
Image.fromarray(np.vstack([first_line, second_line]).astype(np.uint8)).save('out/ex3_xor-otp.png')