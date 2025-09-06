def compter_les_votes(n, k, votes):
    # Initialiser un tableau pour compter les votes pour chaque candidat (index 1 à k)
    compteur_votes = [0] * (k + 1)

    # Compter les votes
    for vote in votes:
        compteur_votes[vote] += 1

    # Calculer le nombre minimum de votes nécessaires pour gagner
    seuil_gagnant = n // 2

    # Vérifier si un candidat a plus de la moitié des votes
    gagnant = "AUCUN"
    for i in range(1, k + 1):
        if compteur_votes[i] > seuil_gagnant:
            gagnant = i
            break

    # Préparer les résultats
    resultats = [compteur_votes[i] for i in range(1, k + 1)]

    # Afficher les résultats
    print(gagnant)
    print(" ".join(map(str, resultats)))

# Exemple d'utilisation
n, k = map(int, input("Entrez le nombre de votants et de candidats : ").split())
votes = list(map(int, input("Entrez les votes : ").split()))
compter_les_votes(n, k, votes)