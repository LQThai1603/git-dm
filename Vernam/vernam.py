def Vernam(Plain,Key,Flag):
    result = ""
    for i in range(len(Plain)):
        char=Plain[i]
        if(Flag):
            result+=chr((ord(char)-97 +ord(Key[i])-97)%26 +97)
        else:
            result += chr((ord(char) - ord(Key[i])+26) % 26 + 97)
    return result

if __name__ == "__main__":
    plain_text = ''.join(input("Enter plain text: ").split())
    key = ''.join(input("Enter key: ").lower().split())

    while 1:
        if (len(key)!=len(plain_text)):
            print('Invalid key!') 
            print("nhập lại")
            key = ''.join(input("Enter key: ").lower().split())  
        else:
            break

    check = []
    for c in plain_text:
        if(c.isupper()):
            check.append(1)
        else:
            check.append(0)
    
    plain_text = plain_text.lower()
    
    cipher_Text = Vernam(plain_text, key, True)

    c1 = ""

    for index, value in enumerate(cipher_Text):
        if check[index] == 1:
            c1 +=value.upper()
        else:
            c1 += value
    
    plain_t = Vernam(cipher_Text,key,False)
    
    p1 = ""

    for index, value in enumerate(plain_t):
        if check[index] == 1:
            p1 +=value.upper()
        else:
            p1 += value

    print("Cipher Text: ", c1)
    print("Plain Text: ", p1)

    