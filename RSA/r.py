import random

max_PrimLength = 1000000000000

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def gcd(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a

def is_prime(num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for n in range(3, int(num**0.5)+2, 2):
        if num % n == 0:
            return False
    return True

def calculate_d(e, phi):
    g, x, y = egcd(e, phi)
    if g != 1:
        raise ValueError("e không phải số nguyên tố cùng phi")
    d = x % phi
    if d < 0:
        d += phi
    return d

def generate_keyPairs(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)
    print ("p = ", p, " q = ", q)
    print("n =", n)
    print("phi =", phi)
    
    while True:
        try:
            e = int(input("Nhập e: "))
            if gcd(e, phi) != 1 or e < 1 or e > phi:
                print("Vui lòng nhập lại.")
            else:
                break
        except ValueError:
            print("Vui lòng nhập một số nguyên hợp lệ.")
       
    d = calculate_d(e, phi)

    return ((e, n), (d, n))

def decrypt(ctext, private_key):
    key, n = private_key
    text = [chr(pow(char, key, n)) for char in ctext]
    return "".join(text)

def encrypt(text, public_key):
    key, n = public_key    
    ctext = [pow(ord(char), key, n) for char in text]
    return ctext

if __name__ == '__main__':
    while True:
        p = int(input("Nhập số nguyên tố p: "))
        if is_prime(p):
            break
        else:
            print("p phải là số nguyên tố. Vui lòng nhập lại.")

    while True:
        q = int(input("Nhập số nguyên tố q: "))
        if is_prime(q):
            break
        else:
            print("q phải là số nguyên tố. Vui lòng nhập lại.")

    public_key, private_key = generate_keyPairs(p, q)
    print("Public: ", public_key)
    print("Private: ", private_key)
    text = input("Nhập chuỗi cần mã hóa: ")
    ctext = encrypt(text, public_key)
    print("encrypted =", ctext)
    plaintext = decrypt(ctext, private_key)
    print("decrypted =", plaintext)