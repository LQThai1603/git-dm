def deCrypted(text, k):
    plain_Text = ""
    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()
            # dich chu cai
            decrypted_Char = chr(((ord(char) - ord('a') - k) % 26) + ord('a'))
            if is_upper:
                decrypted_Char = decrypted_Char.upper()
            plain_Text += decrypted_Char
        else:
            plain_Text += char
    return plain_Text

enCrypted_Text = input("Enter plaintext: ")
key = int(input("Enter key: "))
print("Dencrypted: ", deCrypted(enCrypted_Text, key))