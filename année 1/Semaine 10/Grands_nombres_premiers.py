import random

# Étape 1 : Générer un nombre aléatoire à 100 chiffres
def generer_nombre_aleatoire():
    return random.randint(10**99, 10**100 - 1)

# Étape 2 : Test de divisibilité rapide par 2, 3 et 5
def test_divisibilite_rapide(N):
    if N % 2 == 0 or N % 3 == 0 or N % 5 == 0:
        return False
    return True

# Étape 3 : Test de Fermat
def test_fermat(N, k=30):
    # Répéter k fois le test avec des bases aléatoires
    for _ in range(k):
        A = random.randint(2, N - 2)
        if pow(A, N - 1, N) != 1:
            return False
    return True

# Étape 4 : Combiner toutes les étapes pour trouver un nombre premier
def trouver_premier():
    while True:
        # Générer un nombre aléatoire
        N = generer_nombre_aleatoire()
        # Vérifier la divisibilité rapide et le test de Fermat
        if test_divisibilite_rapide(N) and test_fermat(N):
            return N

# Étape 5 : Exécution du code
if __name__ == "__main__":
    print("Recherche d'un grand nombre premier...")
    premier = trouver_premier()
    print("Nombre premier trouvé :", premier)