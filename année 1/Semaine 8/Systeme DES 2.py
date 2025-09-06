def f(x, y):
    # Fonction f non-linéaire sur deux nombres (vous pouvez modifier selon vos besoins)
    return (x * y + 1) % 26

def dechiffrement_des_simplifie(K, T):
    n = len(K)
    texte_dechiffre = ""

    for i in range(0, len(T), n):
        C = T[i:i + n]

        # Convertir en nombres entre 0 et 25
        Ca = [ord(c) - ord('A') for c in C[:n//2]]
        Cb = [ord(c) - ord('A') for c in C[n//2:]]
        Ka = [ord(c) - ord('A') for c in K[:n//2]]
        Kb = [ord(c) - ord('A') for c in K[n//2:]]

        # Calculer Db et Da
        Db = [(Cb[j] - f(Kb[j], Ca[j])) % 26 for j in range(len(Cb))]
        Da = [(Ca[j] - f(Ka[j], Db[j])) % 26 for j in range(len(Ca))]

        # Convertir en caractères et ajouter au texte déchiffré
        M = ''.join(chr(c + ord('A')) for c in Da + Db)
        texte_dechiffre += M

    return texte_dechiffre