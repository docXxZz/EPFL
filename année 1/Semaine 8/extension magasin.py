def gerer_interactions(n, interactions):
    # Dictionnaire pour stocker le nombre de poissons par sorte
    stock = {}
    resultats = []

    for x in interactions:
        if x > 0:
            # Interaction avec un marchand : ajoute du poisson de sorte x
            if x in stock:
                stock[x] += 1
            else:
                stock[x] = 1
            resultats.append("Merci !")
        
        elif x < 0:
            # Interaction avec un client : vend un poisson de sorte -x
            poisson_type = -x
            if poisson_type in stock and stock[poisson_type] > 0:
                stock[poisson_type] -= 1
                if stock[poisson_type] == 0:
                    del stock[poisson_type]  # Supprime si la quantité est 0
                resultats.append("Et voila !")
            else:
                resultats.append("Desole !")
        
        else:
            # Inventaire : compte le nombre de sortes en stock
            resultats.append(str(len(stock)))

    # Affiche chaque résultat pour chaque interaction
    return resultats

# Exemple d'utilisation
n = int(input("Nombre d'interactions : "))
interactions = [int(input()) for _ in range(n)]
resultats = gerer_interactions(n, interactions)
print("\n".join(resultats))