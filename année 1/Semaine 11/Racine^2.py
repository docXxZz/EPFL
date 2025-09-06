def modular_square_root_workflow(P, C_values):
    """
    Programme unique qui :
    1. Vérifie le critère d'Euler pour un nombre premier P.
    2. Calcule les racines carrées modulo P pour une liste de C.
    
    Arguments :
    - P : Nombre premier (> 2) tel que P % 4 == 3.
    - C_values : Liste des valeurs entières à tester.
    """
    # === Étape 1 : Vérification de P ===
    assert P > 2 and all(P % i != 0 for i in range(2, int(P**0.5) + 1)), "P doit être un nombre premier > 2."
    assert P % 4 == 3, "P doit satisfaire P ≡ 3 (mod 4)."
    
    # === Étape 2 : Vérification du critère d’Euler pour tous les C ===
    print(f"Vérification du critère d'Euler pour P = {P}")
    for C in C_values:
        euler_result = pow(C, (P - 1) // 2, P)  # Calcul C^(P-1)/2 % P
        if euler_result == 1:
            print(f"C = {C} satisfait le critère d'Euler (C^((P-1)/2) % P = 1).")
        elif euler_result == P - 1:
            print(f"C = {C} ne satisfait pas le critère d'Euler (C^((P-1)/2) % P = P - 1). Aucune racine carrée.")
        else:
            print(f"Erreur inattendue pour C = {C}.")
    
    # === Étape 3 : Calcul des racines carrées modulo P ===
    print(f"\nCalcul des racines carrées pour P = {P} :")
    for C in C_values:
        try:
            # Vérification du critère d’Euler avant le calcul
            if pow(C, (P - 1) // 2, P) != 1:
                raise ValueError(f"C = {C} ne satisfait pas le critère d'Euler.")
            
            # Calcul de la racine carrée modulo P
            M = pow(C, (P + 1) // 4, P)
            print(f"Pour C = {C}, une racine carrée modulo {P} est M = {M}. Vérification : M^2 % P = {M**2 % P}")
        except ValueError as e:
            print(e)

# === Exemple d'utilisation ===
P = 7  # Nombre premier (P % 4 == 3)
C_values = [1, 2, 3, 4, 5, 6]  # Liste des valeurs de C à tester
modular_square_root_workflow(P, C_values)