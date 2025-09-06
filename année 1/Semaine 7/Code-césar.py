def dechiffrer_cesar(texte_chiffre, decalage):
    texte_dechiffre = ""
    
    # Parcourt chaque caractère du texte chiffré
    for char in texte_chiffre:
        # Vérifie si le caractère est une lettre majuscule
        if char.isupper():
            texte_dechiffre += chr((ord(char) - decalage - 65) % 26 + 65)
        # Vérifie si le caractère est une lettre minuscule
        elif char.islower():
            texte_dechiffre += chr((ord(char) - decalage - 97) % 26 + 97)
        else:
            # Conserve les caractères non alphabétiques sans les décaler
            texte_dechiffre += char
            
    return texte_dechiffre

# Exemple d'utilisation
texte_chiffre = "ENCRYPTER"  # "Hello World" chiffré avec un décalage de 3
decalage = 3
texte_dechiffre = dechiffrer_cesar(texte_chiffre, decalage)
print("Texte déchiffré :", texte_dechiffre)