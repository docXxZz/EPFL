def dechiffrer_vigenere(texte_chiffre, cle):
    texte_dechiffre = ""
    cle = cle.lower()  # On convertit la clé en minuscule pour simplifier le calcul
    index_cle = 0

    for char in texte_chiffre:
        # Vérifie si le caractère est une lettre majuscule
        if char.isupper():
            decalage = ord(cle[index_cle % len(cle)]) - ord('a')
            texte_dechiffre += chr((ord(char) - decalage - 65) % 26 + 65)
            index_cle += 1
        # Vérifie si le caractère est une lettre minuscule
        elif char.islower():
            decalage = ord(cle[index_cle % len(cle)]) - ord('a')
            texte_dechiffre += chr((ord(char) - decalage - 97) % 26 + 97)
            index_cle += 1
        else:
            # Conserve les caractères non alphabétiques sans les décaler
            texte_dechiffre += char

    return texte_dechiffre

# Exemple d'utilisation
texte_chiffre = "NH FZQOGUKMHX XMK CAK FUTPVTX KLQ CKNN VBEK ILFOEGFGVM CUNL VNSKVNLME GNNFUNZBKLMZKGN UMF YXKLMAIXM U WCKKUKQBTL UIQGNFYKQDAXM FC YUZCHCRY EYJ WEJBHRBRAKM VTRIMLFVVWNYJ VHSXLZYHKL GFLRXGYJ XRAOYEB RLYYTBHKK XVA RTLYDJYKL AVVRXBKLMF J HJVZNZBIEA PUGHLA PUFGV XEUZLRUZKL WVA CXHAIIZSXM GMESXNKMAZ TOO WEJBHRBRAKM U MKKVOKME AGY CIEMX YMMAZTCC LR ZTWYMF AG MPAGKFY ZVSUKGRBVWNY VAG THGZVNRXGVVG AG IILVTTNVCE IHGGTRZ JOZ KBSILVVQ RX GRBRXBYC TR YRMKMZK W YOXYUBNRBVUG YK T RWNCGMZKGN GMEOIBVZVWNY EMPKLMRQEKL YK CGOECJMF VHOI CA LHHTBVUGHVURTM WFUCRXN TM GKKGV XRAM YXIYKFYEB FK KYWMEKK U LV TXHOGM QGHLUQAGMYLZF RBYJ MG LHHTBVUGHRVG KGMVUORX WFUZK NH IMFKTO ZVSUKGRBVWNY FC HT VFLAGKK X FZQOGUKMHX"  # "Hello World" chiffré avec la clé "KEY"
cle = "TURING"
texte_dechiffre = dechiffrer_vigenere(texte_chiffre, cle)
print("Texte déchiffré :", texte_dechiffre)