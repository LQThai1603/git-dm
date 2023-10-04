def enCrypted(text, k):
    cipher_Text = ""
    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()
            # Dich chu cai
            encrypted_Char = chr((ord(char) + k - ord('a')) % 26 + ord('a'))
            if is_upper:
                encrypted_Char = encrypted_Char.upper()
            cipher_Text += encrypted_Char
        else:
            cipher_Text += char
    return cipher_Text 
plan_Text = input("Enter plaintext: ")
key = int(input("Enter key: "))
print("Encrypted: ", enCrypted(plan_Text, key))