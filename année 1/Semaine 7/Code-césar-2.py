from collections import Counter

def dechiffrer_cesar_par_frequence(texte_chiffre):
    # Compte les fréquences des lettres dans le texte chiffré
    compteur_lettres = Counter(char for char in texte_chiffre.lower() if char.isalpha())
    
    # Trouve la lettre la plus fréquente dans le texte chiffré
    lettre_frequente_chiffree = compteur_lettres.most_common(1)[0][0]
    
    # Calcul du décalage en supposant que la lettre la plus fréquente dans le texte chiffré correspond à 'e'
    decalage = (ord(lettre_frequente_chiffree) - ord('e')) % 26
    
    # Déchiffre le texte avec le décalage trouvé
    texte_dechiffre = ""
    for char in texte_chiffre:
        if char.isupper():
            texte_dechiffre += chr((ord(char) - decalage - 65) % 26 + 65)
        elif char.islower():
            texte_dechiffre += chr((ord(char) - decalage - 97) % 26 + 97)
        else:
            texte_dechiffre += char
            
    return texte_dechiffre, decalage

# Exemple d'utilisation
texte_chiffre = "IB CFRWBOHSIF SGH IBS AOQVWBS EIW DSIH SHFS DFCUFOAASS DCIF STTSQHISF OIHCAOHWEISASBH RSG GSEISBQSG R CDSFOHWCBG OFWHVASHWEISG CI ZCUWEISG ZSG CFRWBOHSIFG SZSQHFCBWEISG BIASFWEISG ACRSFBSG DSIJSBH STTSQHISF RSG SBGSAPZSG USBSFWEISG R CDSFOHWCBG QCBBIG QCAAS DFCUFOAASG QSG DFCUFOAASG DSFASHHSBH OIL CFRWBOHSIFG R SLSQIHSF IBS ZOFUS SJSBHOWZ RS HOQVSG IB GMGHSAS WBTCFAOHWEIS SGH BCAWBOZSASBH IB CFRWBOHSIF QCADZSH EIW QCADFSBR ZS AOHSFWSZ ZS GMGHSAS R SLDZCWHOHWCB SH Z SEIWDSASBH DSFWDVSFWEIS BSQSGGOWFSG SH IHWZWGSG DCIF IB TCBQHWCBBSASBH QCADZSH QS HSFAS DSIH SUOZSASBH GS FSTSFSF O IB UFCIDS ROCFRWBOHSIFG ZWSG SH TCBQHWCBBOBH SBGSAPZS QCAAS IB FSGSOI WBTCFAOHWEIS CI IB QZIGHSF R CFRWBOHSIF"  # "Hello World" chiffré avec un décalage de 3
texte_dechiffre, decalage_trouve = dechiffrer_cesar_par_frequence(texte_chiffre)
print("Texte déchiffré :", texte_dechiffre)
print("Décalage trouvé :", decalage_trouve)