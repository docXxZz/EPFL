def xorshift32(seed, iterations):
    """
    Implémente l'algorithme Xorshift pour générer une séquence de nombres aléatoires 32 bits.

    :param seed: La graine (entier 32 bits, non nul).
    :param iterations: Le nombre de nombres à générer.
    :return: Une liste de nombres aléatoires de 32 bits.
    """
    if seed == 0:
        raise ValueError("La graine doit être un entier non nul.")

    # Liste pour stocker les résultats
    sequence = []

    # Masque pour limiter à 32 bits
    MASK = 0xFFFFFFFF  # Correspond à 2^32 - 1

    # Génération des nombres
    x = seed
    for _ in range(iterations):
        x ^= (x << 13) & MASK  # Décalage vers la gauche et XOR
        x ^= (x >> 17) & MASK  # Décalage vers la droite et XOR
        x ^= (x << 5) & MASK   # Décalage vers la gauche et XOR
        x &= MASK              # Limiter à 32 bits
        sequence.append(x)

    return sequence

def afficher_resultats(sequence):
    """
    Affiche la séquence générée et son histogramme.

    :param sequence: La liste des nombres générés.
    """
    import matplotlib.pyplot as plt

    # Graphique 1 : Liste des nombres générés
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.plot(sequence, ".-", color="blue")
    plt.title("Séquence de nombres générés")
    plt.xlabel("Index")
    plt.ylabel("Valeur")

    # Graphique 2 : Histogramme des valeurs
    plt.subplot(1, 2, 2)
    plt.hist(sequence, bins=50, color="skyblue", edgecolor="black")
    plt.title("Histogramme des nombres générés")
    plt.xlabel("Valeur")
    plt.ylabel("Fréquence")

    plt.tight_layout()
    plt.show()

# Entrée utilisateur
seed = int(input("Entrez une graine non nulle (entier 32 bits) : "))
iterations = int(input("Entrez le nombre de nombres à générer : "))

# Vérification de la graine
if seed <= 0 or seed > 0xFFFFFFFF:
    print("La graine doit être un entier compris entre 1 et 2^32 - 1.")
else:
    # Génération et affichage des résultats
    sequence = xorshift32(seed, iterations)
    print("Séquence générée :", sequence)
    afficher_resultats(sequence)