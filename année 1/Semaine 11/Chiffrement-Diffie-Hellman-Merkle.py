import random

def diffie_hellman_encrypt_decrypt(n, message):
    # === Étape 1 : Génération de la clé avec Diffie-Hellman-Merkle ===
    def generate_key_diffie_hellman(n):
        p = 26 ** n  # Modulo
        g = 5  # Générateur arbitraire
        # Clés privées
        a = random.randint(1, p-1)
        b = random.randint(1, p-1)
        # Clés publiques
        A = pow(g, a, p)
        B = pow(g, b, p)
        # Clé commune
        K_alice = pow(B, a, p)
        K_bob = pow(A, b, p)
        assert K_alice == K_bob, "Erreur : Les clés calculées par Alice et Bob ne correspondent pas !"
        return K_alice

    # === Étape 2 : Transformer la clé en une liste ===
    def transform_key_to_list(K, n):
        key_list = []
        for _ in range(n):
            key_list.append(K % 26)
            K //= 26
        return key_list[::-1]

    # === Étape 3 : Chiffrement et déchiffrement ===
    def text_to_numbers(text):
        return [ord(char) - ord('A') for char in text.upper()]

    def numbers_to_text(numbers):
        return ''.join(chr(num + ord('A')) for num in numbers)

    def encrypt_message(message, key):
        message_numbers = text_to_numbers(message)
        encrypted_numbers = [(m + k) % 26 for m, k in zip(message_numbers, key)]
        return numbers_to_text(encrypted_numbers)

    def decrypt_message(encrypted_message, key):
        encrypted_numbers = text_to_numbers(encrypted_message)
        decrypted_numbers = [(e - k) % 26 for e, k in zip(encrypted_numbers, key)]
        return numbers_to_text(decrypted_numbers)

    # === Exécution des étapes ===
    # Génération de la clé Diffie-Hellman
    K = generate_key_diffie_hellman(n)
    key_list = transform_key_to_list(K, n)

    # Chiffrement
    encrypted_message = encrypt_message(message, key_list)
    print("Message original :", message)
    print("Message chiffré :", encrypted_message)

    # Déchiffrement
    decrypted_message = decrypt_message(encrypted_message, key_list)
    print("Message déchiffré :", decrypted_message)

    # Vérification
    assert decrypted_message == message, "Erreur : le message déchiffré ne correspond pas au message original !"

# === Exemple d'utilisation ===
n = 5  # Longueur de la clé
message = "HELLO"  # Message à chiffrer
diffie_hellman_encrypt_decrypt(n, message)