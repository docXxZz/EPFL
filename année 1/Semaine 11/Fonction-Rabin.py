def extended_euclidean(a, b):
    """Implémentation de l'algorithme d'Euclide étendu pour trouver X et Y tels que a*X + b*Y = gcd(a, b)."""
    if b == 0:
        return a, 1, 0
    gcd, x1, y1 = extended_euclidean(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return gcd, x, y

def modular_square_root_rabin(C, P, Q):
    """
    Calcule les racines carrées de C modulo N, où N = P * Q.
    Arguments :
    - C : Nombre dont on veut trouver les racines carrées.
    - P, Q : Nombres premiers tels que P % 4 == 3 et Q % 4 == 3.
    Retourne : Les quatre racines R1, R2, R3, R4 modulo N.
    """
    assert P % 4 == 3 and Q % 4 == 3, "P et Q doivent satisfaire P % 4 == 3 et Q % 4 == 3."
    
    # Calcul de N
    N = P * Q

    # Étape 1 : Calcul des racines carrées modulo P et Q
    MP = pow(C, (P + 1) // 4, P)  # Racine carrée modulo P
    MQ = pow(C, (Q + 1) // 4, Q)  # Racine carrée modulo Q

    # Étape 2 : Calcul des coefficients XP et XQ à l'aide de l'algorithme d'Euclide étendu
    _, XP, XQ = extended_euclidean(P, Q)

    # Étape 3 : Calcul des racines modulo N
    R1 = (XP * P * MQ + XQ * Q * MP) % N
    R2 = N - R1
    R3 = (XP * P * MQ - XQ * Q * MP) % N
    R4 = N - R3

    return R1, R2, R3, R4

def rabin_encrypt_decrypt(message, P, Q):
    """
    Implémente le cryptosystème de Rabin :
    - Chiffre le message en utilisant C = M^2 mod N.
    - Déchiffre le message pour retrouver les racines carrées.
    Arguments :
    - message : Le message à chiffrer (entier).
    - P, Q : Nombres premiers pour le cryptosystème.
    """
    # Calcul de N
    N = P * Q

    # Chiffrement
    C = (message ** 2) % N
    print(f"Message chiffré (C) : {C}")

    # Déchiffrement
    R1, R2, R3, R4 = modular_square_root_rabin(C, P, Q)
    print(f"Racines possibles : R1 = {R1}, R2 = {R2}, R3 = {R3}, R4 = {R4}")

    # Identification du bon message parmi les quatre racines
    possible_messages = {R1, R2, R3, R4}
    if message in possible_messages:
        print(f"Message original retrouvé : {message}")
    else:
        print(f"Le message original ({message}) est ambigu parmi les racines possibles.")

# === Exemple d'utilisation ===
P = 7  # Nombre premier P
Q = 11  # Nombre premier Q
message = 5  # Message à chiffrer (doit être plus petit que N = P * Q)

rabin_encrypt_decrypt(message, P, Q)