def f(x, y):
    # Fonction f non-linéaire sur deux nombres (vous pouvez modifier selon vos besoins)
    return (x * y + 1) % 26

def chiffrement_des_simplifie(K, T):
    n = len(K)
    texte_chiffre = ""

    for i in range(0, len(T), n):
        M = T[i:i + n]
        
        # Convertir en nombres entre 0 et 25
        Ma = [ord(c) - ord('A') for c in M[:n//2]]
        Mb = [ord(c) - ord('A') for c in M[n//2:]]
        Ka = [ord(c) - ord('A') for c in K[:n//2]]
        Kb = [ord(c) - ord('A') for c in K[n//2:]]

        # Calculer Ca et Cb
        Ca = [(Ma[j] + f(Ka[j], Mb[j])) % 26 for j in range(len(Ma))]
        Cb = [(Mb[j] + f(Kb[j], Ca[j])) % 26 for j in range(len(Mb))]

        # Convertir en caractères et ajouter au texte chiffré
        C = ''.join(chr(c + ord('A')) for c in Ca + Cb)
        texte_chiffre += C

    return texte_chiffre