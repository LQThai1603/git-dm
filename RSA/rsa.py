import random

max_PrimLength = 1000000000000

def is_prime(num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for n in range(3, int(num**0.5)+2, 2):
        if num % n == 0:
            return False
    return True

def generateRandomPrim():
    while True:
        ranPrime = random.randint(0, max_PrimLength)
        if is_prime(ranPrime):
            return ranPrime

def generate_keypair(p, q):
    n = p * q
    phi = (p-1) * (q-1)
    # Chon e sao cho 1 < e < phi va ucln(e, phi) = 1
    e = random.randint(1, phi)
    while gcd(e, phi) != 1:
        e = random.randint(1, phi)
    # Tinh sao d cho de % phi = 1
    # Calculate d, which is the modular inverse of e mod phi
    d = mod_inverse(e, phi)
    
    return (e, n), (d, n)
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
def mod_inverse(a, m):
    # Thuat toan eculid mo rong
    if gcd(a, m) != 1:
        return None
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m
    while v3 != 0:
        q = u3 // v3
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
    
    return u1 % m
def encrypt(plaintext, public_key):
    e, n = public_key
    ciphertext = [pow(ord(c), e, n) for c in plaintext]
    return ciphertext
def decrypt(ciphertext, private_key):
    d, n = private_key
    plaintext = [chr(pow(c, d, n)) for c in ciphertext]
    return ''.join(plaintext)

# Vi du
p = generateRandomPrim()
q = generateRandomPrim()
public_key, private_key = generate_keypair(p, q)
#message = "How are you?"
message = input("nhập chuỗi mesage: ")
ciphertext = encrypt(message, public_key)
decrypted_message = decrypt(ciphertext, private_key)
print("Public key:", public_key)
print("Private key:", private_key)
print("Ciphertext:", ciphertext)
print("Decrypted message:", decrypted_message)