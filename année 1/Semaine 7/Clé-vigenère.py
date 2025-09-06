import re
from collections import Counter

# Fréquence des lettres en français (en pourcentages)
french_letter_freq = {
    'E': 14.7, 'A': 7.6, 'I': 7.5, 'S': 7.9, 'N': 7.0, 'R': 6.5, 'T': 7.0, 'O': 5.8,
    'L': 5.5, 'U': 6.3, 'D': 3.6, 'C': 3.3, 'M': 2.7, 'P': 3.1, 'G': 1.0, 'B': 1.1,
    'V': 1.7, 'H': 1.1, 'F': 1.1, 'Q': 0.9, 'Y': 0.5, 'X': 0.4, 'J': 0.3, 'K': 0.0, 'Z': 0.1
}

def vigenere_decrypt(ciphertext, key):
    decrypted_text = ""
    key_length = len(key)
    for i, char in enumerate(ciphertext):
        if char.isalpha():
            offset = ord('A') if char.isupper() else ord('a')
            decrypted_text += chr((ord(char) - offset - (ord(key[i % key_length].lower()) - ord('a'))) % 26 + offset)
        else:
            decrypted_text += char
    return decrypted_text

def calculate_frequency_score(text):
    text = text.upper()
    letter_counts = Counter([char for char in text if char.isalpha()])
    total_letters = sum(letter_counts.values())
    frequency_diff = 0.0
    
    for letter, freq in french_letter_freq.items():
        observed_freq = (letter_counts.get(letter, 0) / total_letters) * 100 if total_letters > 0 else 0
        frequency_diff += abs(observed_freq - freq)
    
    return frequency_diff

def find_best_key_for_position(segment):
    best_shift = 0
    best_score = float('inf')
    best_letter = 'A'
    
    for shift in range(26):
        decrypted_segment = ''.join(
            chr(((ord(char) - ord('A') - shift) % 26) + ord('A')) for char in segment
        )
        score = calculate_frequency_score(decrypted_segment)
        
        if score < best_score:
            best_score = score
            best_shift = shift
            best_letter = chr(best_shift + ord('A'))
    
    return best_letter

def find_key(ciphertext, key_length):
    key = ""
    for i in range(key_length):
        segment = "".join([ciphertext[j] for j in range(i, len(ciphertext), key_length)])
        best_letter = find_best_key_for_position(segment)
        key += best_letter
    return key

def reinsert_spaces(text, space_positions):
    # Réinsère les espaces aux positions d'origine
    spaced_text = list(text)
    for pos in space_positions:
        spaced_text.insert(pos, " ")
    return ''.join(spaced_text)

def main(ciphertext):
    # Enregistre les positions des espaces dans le texte chiffré
    space_positions = [pos for pos, char in enumerate(ciphertext) if char == " "]
    
    # Supprime les espaces pour le déchiffrement
    ciphertext = re.sub(r'[^A-Za-z]', '', ciphertext).upper()
    
    best_key = ""
    best_score = float('inf')
    best_decrypted_text = ""
    
    # Tester des longueurs de clé de 1 à 20
    for key_length in range(1, 21):
        key = find_key(ciphertext, key_length)
        decrypted_text = vigenere_decrypt(ciphertext, key)
        score = calculate_frequency_score(decrypted_text)
        
        if score < best_score:
            best_score = score
            best_key = key
            best_decrypted_text = decrypted_text

    # Réinsère les espaces aux positions d'origine
    final_decrypted_text = reinsert_spaces(best_decrypted_text, space_positions)
    
    print("Meilleure clé estimée :", best_key)
    print("Texte déchiffré :", final_decrypted_text)

# Exemple d'utilisation
ciphertext = "NH FZQOGUKMHX XMK CAK FUTPVTX KLQ CKNN VBEK ILFOEGFGVM CUNL VNSKVNLME GNNFUNZBKLMZKGN UMF YXKLMAIXM U WCKKUKQBTL UIQGNFYKQDAXM FC YUZCHCRY EYJ WEJBHRBRAKM VTRIMLFVVWNYJ VHSXLZYHKL GFLRXGYJ XRAOYEB RLYYTBHKK XVA RTLYDJYKL AVVRXBKLMF J HJVZNZBIEA PUGHLA PUFGV XEUZLRUZKL WVA CXHAIIZSXM GMESXNKMAZ TOO WEJBHRBRAKM U MKKVOKME AGY CIEMX YMMAZTCC LR ZTWYMF AG MPAGKFY ZVSUKGRBVWNY VAG THGZVNRXGVVG AG IILVTTNVCE IHGGTRZ JOZ KBSILVVQ RX GRBRXBYC TR YRMKMZK W YOXYUBNRBVUG YK T RWNCGMZKGN GMEOIBVZVWNY EMPKLMRQEKL YK CGOECJMF VHOI CA LHHTBVUGHVURTM WFUCRXN TM GKKGV XRAM YXIYKFYEB FK KYWMEKK U LV TXHOGM QGHLUQAGMYLZF RBYJ MG LHHTBVUGHRVG KGMVUORX WFUZK NH IMFKTO ZVSUKGRBVWNY FC HT VFLAGKK X FZQOGUKMHX"  # Remplacez ceci par le texte chiffré
main(ciphertext)