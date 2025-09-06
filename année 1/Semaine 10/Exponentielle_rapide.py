def expo_mod_iterative(A, B, N):
    """
    Calcule efficacement A^B (mod N) en utilisant l'exponentiation rapide (version itérative).
    """
    result = 1  # Résultat initial
    base = A % N  # Réduction initiale de A modulo N

    while B > 0:
        # Si le bit courant de B est 1, multiplier par la base
        if B % 2 == 1:
            result = (result * base) % N
        
        # Passer au bit suivant et élever la base au carré
        base = (base * base) % N
        B //= 2  # Décalage à droite des bits de B

    return result

def expo_mod_recursive(A, B, N):
    """
    Calcule efficacement A^B (mod N) en utilisant l'exponentiation rapide (version récursive).
    """
    if B == 0:
        return 1  # Cas de base : A^0 = 1
    if B % 2 == 0:
        # Si B est pair, on calcule (A^(B/2))^2 (mod N)
        half = expo_mod_recursive(A, B // 2, N)
        return (half * half) % N
    else:
        # Si B est impair, on calcule A * A^(B-1) (mod N)
        return (A * expo_mod_recursive(A, B - 1, N)) % N

def main():
    """
    Fonction principale pour tester les deux versions de l'exponentiation modulaire.
    """
    # Exemple : paramètres d'entrée
    A = 7
    B = 560
    N = 13

    print("Exponentiation rapide : A^B (mod N)")
    print(f"Entrées : A = {A}, B = {B}, N = {N}\n")

    # Calcul avec la version itérative
    resultat_iteratif = expo_mod_iterative(A, B, N)
    print(f"Résultat (itératif) : {resultat_iteratif}")

    # Calcul avec la version récursive
    resultat_recursif = expo_mod_recursive(A, B, N)
    print(f"Résultat (récursif) : {resultat_recursif}")

# Exécution du programme
if __name__ == "__main__":
    main()