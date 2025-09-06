import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

def hough_transform(image_path, num_rho=180, num_phi=180):
    # Charger l'image et la convertir en niveaux de gris
    image = Image.open(image_path).convert('L')
    image_array = np.array(image)
    
    # Détection des contours (par exemple, avec un seuil simple)
    edges = (image_array > 128).astype(np.uint8)  # Seuil simple pour binariser
    
    # Calcul de la diagonale de l'image (valeur maximale de rho)
    height, width = edges.shape
    diag_len = np.ceil(np.sqrt(height**2 + width**2)).astype(int)
    
    # Créer les listes de rho et phi
    rhos = np.linspace(-diag_len, diag_len, num_rho)
    phis = np.linspace(-np.pi / 2, np.pi / 2, num_phi)
    
    # Initialisation de l'accumulateur
    accumulator = np.zeros((num_rho, num_phi), dtype=np.int)
    
    # Algorithme de Hough
    for y in range(height):
        for x in range(width):
            if edges[y, x]:  # Si le pixel appartient à un contour
                for phi_idx, phi in enumerate(phis):
                    rho = x * np.cos(phi) + y * np.sin(phi)
                    rho_idx = np.argmin(np.abs(rhos - rho))  # Trouver l'indice de rho le plus proche
                    accumulator[rho_idx, phi_idx] += 1

    return accumulator, rhos, phis

def plot_hough_space(accumulator, rhos, phis):
    plt.imshow(accumulator, extent=[phis[0], phis[-1], rhos[-1], rhos[0]], aspect='auto', cmap='hot')
    plt.title('Espace de Hough')
    plt.xlabel('Phi (radians)')
    plt.ylabel('Rho (pixels)')
    plt.colorbar(label='Votes')
    plt.show()

# Exemple d'utilisation
image_path = "/Users/daniel/Library/Mobile Documents/com~apple~CloudDocs/EPFL/Code/Semaine 16/CT-100 Exercise Images Week 16.zip"  # Remplacez par le chemin de votre image
accumulator, rhos, phis = hough_transform(image_path)
plot_hough_space(accumulator, rhos, phis)