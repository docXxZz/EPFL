def chiffrer_vigenere(texte, cle):
    texte_chiffre = ""
    cle = cle.lower()  # On convertit la clé en minuscule pour simplifier le calcul
    index_cle = 0

    for char in texte:
        # Vérifie si le caractère est une lettre majuscule
        if char.isupper():
            decalage = ord(cle[index_cle % len(cle)]) - ord('a')
            texte_chiffre += chr((ord(char) + decalage - 65) % 26 + 65)
            index_cle += 1
        # Vérifie si le caractère est une lettre minuscule
        elif char.islower():
            decalage = ord(cle[index_cle % len(cle)]) - ord('a')
            texte_chiffre += chr((ord(char) + decalage - 97) % 26 + 97)
            index_cle += 1
        else:
            # Conserve les caractères non alphabétiques sans les décaler
            texte_chiffre += char

    return texte_chiffre

# Exemple d'utilisation
texte = "ENCRYPTER BC UN PETIT TEXTE"
cle = "KEY"
texte_chiffre = chiffrer_vigenere(texte, cle)
print("Texte chiffré :", texte_chiffre)