import matplotlib.pyplot as plt

def generer_suite_modulaire(m, a, b, n):
    """
    Génère une suite de nombres selon la formule (ax + b) % m.

    :param m: Modulo (entier positif).
    :param a: Coefficient multiplicatif.
    :param b: Constante additive.
    :param n: Nombre d'itérations.
    :return: Une liste des nombres générés.
    """
    x = 1  # Point de départ
    suite = []
    for _ in range(n):
        x = (a * x + b) % m
        suite.append(x)
    return suite

def tracer_resultats(suite, m, a, b):
    """
    Trace les graphiques demandés à partir de la suite générée.

    :param suite: Liste des nombres générés.
    :param m: Modulo utilisé.
    :param a: Coefficient multiplicatif.
    :param b: Constante additive.
    """
    # Liste des indices
    indices = list(range(1, len(suite) + 1))

    # Graphique 1 : Liste des nombres générés
    plt.figure(figsize=(12, 4))
    plt.subplot(1, 3, 1)
    plt.plot(indices, suite, ".-", color="blue")
    plt.title("Liste des nombres générés")
    plt.xlabel("Index")
    plt.ylabel("Valeur")

    # Graphique 2 : Histogramme des valeurs
    plt.subplot(1, 3, 2)
    plt.hist(suite, bins=range(min(suite), max(suite) + 2), color="skyblue", edgecolor="black")
    plt.title("Histogramme des nombres générés")
    plt.xlabel("Valeur")
    plt.ylabel("Fréquence")

    # Graphique 3 : Graphe des points (x, (ax + b) % m)
    plt.subplot(1, 3, 3)
    y_values = [(a * x + b) % m for x in suite]
    plt.plot(suite, y_values, ".", color="green")
    plt.title("Graphe des points")
    plt.xlabel("x")
    plt.ylabel("(ax + b) % m")

    plt.tight_layout()
    plt.show()

# Entrée utilisateur
m = int(input("Entrez la valeur de m (modulo) : "))
a = int(input("Entrez la valeur de a (coefficient multiplicatif) : "))
b = int(input("Entrez la valeur de b (constante additive) : "))
n = int(input("Entrez le nombre d'itérations : "))

# Génération de la suite et tracés
if m <= 0:
    print("La valeur de m doit être un entier positif.")
else:
    suite = generer_suite_modulaire(m, a, b, n)
    print("Suite générée :", suite)
    tracer_resultats(suite, m, a, b)