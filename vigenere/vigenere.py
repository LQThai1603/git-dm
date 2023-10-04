def vingenere(plain_text, s, Flag):
    result = ""
    for i in range(len(plain_text)):
        char = plain_text[i]
        if (Flag):
            result+=chr((ord(char)-97 + ord(s[i]) - 97) % 26 + 97)
        else:
            result += chr((ord(char) - ord(s[i]) + 26) % 26 + 97)
    return result



if __name__ == "__main__":
    key = ''.join(input("Enter key: ").lower().split())
    plain_text = ''.join(input("Enter plain text: ").split())

    check = []
    for c in plain_text:
        if(c.isupper()):
            check.append(1)
        else:
            check.append(0)

    plain_text = plain_text.lower()

    s=''
    caterpillar=0
    for i in range(len(plain_text)):
        s+=key[caterpillar%len(key)]
        caterpillar+=1
    cipher_text = vingenere(plain_text,s,True)
    c1 = ""

    for index, value in enumerate(cipher_text):
        if check[index] == 1:
            c1 +=value.upper()
        else:
            c1 += value


    plain_t = vingenere(cipher_text,s,False)

    p1 = ""

    for index, value in enumerate(plain_t):
        if check[index] == 1:
            p1 +=value.upper()
        else:
            p1 += value

    print("Cipher Text: ", c1)
    print("Plain Text: ", p1)
