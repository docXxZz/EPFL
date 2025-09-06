import random

def chiffrement_cle_unique(M, K):
    C = ""
    for i in range(len(M)):
        prob = random.random()
        if prob < 0.5:
            # Ci = Mi
            C += M[i]
        else:
            # Ci = Mi + Ki (mod 26)
            C += chr(((ord(M[i]) - ord('A') + ord(K[i]) - ord('A')) % 26) + ord('A'))
    return C