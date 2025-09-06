def verifier_pente_uniforme(n, hauteurs):
    if n <= 2:
        return "OUI"  # Avec un ou deux piliers, la pente est forcément régulière
    
    # Calcul de la pente initiale
    pente = hauteurs[1] - hauteurs[0]
    
    # Vérification de la pente entre chaque paire de piliers
    for i in range(2, n):
        if hauteurs[i] - hauteurs[i - 1] != pente:
            return "NON"
    
    return "OUI"

# Exemple d'utilisation
n = int(input("Entrez le nombre de piliers : "))
hauteurs = list(map(int, input("Entrez les hauteurs des piliers : ").split()))
print(verifier_pente_uniforme(n, hauteurs))