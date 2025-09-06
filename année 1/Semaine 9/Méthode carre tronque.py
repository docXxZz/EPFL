import matplotlib.pyplot as plt

def extraire_milieu(nombre, longueur=8):
    """
    Extrait les `longueur` chiffres du milieu d'un nombre donné.

    :param nombre: Le nombre à partir duquel extraire les chiffres.
    :param longueur: La longueur des chiffres à extraire (par défaut 8).
    :return: Les chiffres du milieu sous forme d'entier.
    """
    nombre_str = str(nombre)
    total_len = len(nombre_str)
    
    # Vérifier que le carré est assez long
    if total_len < longueur:
        raise ValueError("Le carré n'a pas suffisamment de chiffres pour extraire le milieu.")
    
    # Calculer les indices de début et de fin
    debut = (total_len - longueur) // 2
    fin = debut + longueur
    return int(nombre_str[debut:fin])

def generer_suite(nombre_initial, iterations):
    """
    Génère une suite de nombres à partir d'un nombre initial en appliquant la méthode des chiffres du milieu.

    :param nombre_initial: Le nombre initial (doit être un entier de 8 chiffres).
    :param iterations: Le nombre d'itérations à effectuer.
    :return: Une liste des nombres générés.
    """
    suite = []
    nombre = nombre_initial

    for _ in range(iterations):
        carre = nombre ** 2
        try:
            nombre = extraire_milieu(carre, longueur=8)
            suite.append(nombre)
        except ValueError as e:
            print(f"Erreur : {e}")
            break

    return suite

def afficher_histogramme(suite):
    """
    Affiche l'histogramme des nombres générés.

    :param suite: La liste des nombres générés.
    """
    plt.hist(suite, bins=range(min(suite), max(suite) + 1), color='skyblue', edgecolor='black')
    plt.title("Histogramme des nombres générés")
    plt.xlabel("Nombre")
    plt.ylabel("Fréquence")
    plt.show()

# Entrée utilisateur
nombre_initial = int(input("Entrez un nombre initial à 8 chiffres : "))
iterations = int(input("Entrez le nombre d'itérations : "))

# Vérification que le nombre initial est valide
if not (10**7 <= nombre_initial < 10**8):
    print("Le nombre initial doit avoir exactement 8 chiffres.")
else:
    # Génération de la suite et affichage de l'histogramme
    suite = generer_suite(nombre_initial, iterations)
    print("Suite générée :", suite)
    afficher_histogramme(suite)