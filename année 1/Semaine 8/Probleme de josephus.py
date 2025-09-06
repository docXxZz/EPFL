def dernier_soldat(n):
    # Trouver la plus grande puissance de 2 <= n
    puissance_deux = 1
    while puissance_deux <= n:
        puissance_deux *= 2
    puissance_deux //= 2

    # Calculer la position du dernier soldat
    return 2 * (n - puissance_deux) + 1

# Entrée du nombre de soldats
n = int(input("Entrez le nombre de soldats : "))
print("Le dernier survivant est le soldat numéro :", dernier_soldat(n))