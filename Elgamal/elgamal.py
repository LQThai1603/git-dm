# Hàm tính nghịch đảo modulo
def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

# Hàm kiểm tra xem một số có phải là số nguyên tố không
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# Hàm kiểm tra xem một số có phải là phần tử nguyên thuỷ modulo p không
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def is_primitive_root(a, p):
    if gcd(a, p) != 1:
        return False

    phi_p = p - 1
    factors = set()

    # Tính các ước số của phi(p)
    for i in range(2, int(phi_p ** 0.5) + 1):
        if phi_p % i == 0:
            factors.add(i)
            factors.add(phi_p // i)

    # Kiểm tra xem a^(phi(p)/q) (với q là các ước số của phi(p)) khác 1 (mod p)
    for factor in factors:
        if pow(a, phi_p // factor, p) == 1:
            return False
    print(factors)
    return True

# Nhập và kiểm tra giá trị p (số nguyên tố)
while True:
    try:
        p = int(input("Nhập số nguyên tố p: "))
        if is_prime(p):
            break
        else:
            print("p không phải là số nguyên tố. Hãy nhập lại.")
    except ValueError:
        print("Giá trị không hợp lệ. Hãy nhập lại.")

# Nhập giá trị a (khóa bí mật)
while True:
    try:
        a = int(input("Nhập khóa bí mật a (số nguyên dương < p): "))
        if 0 < a < p:
            break
        else:
            print("a phải là số nguyên dương nhỏ hơn p. Hãy nhập lại.")
    except ValueError:
        print("Giá trị không hợp lệ. Hãy nhập lại.")

# Nhập giá trị g (phần tử nguyên thuỷ modulo p)
while True:
    try:
        g = int(input("Nhập phần tử nguyên thuỷ g (số nguyên < p): "))
        if 0 < g < p and is_primitive_root(g, p):
            break
        else:
            print("g phải là số nguyên dương nguyên thuỷ nhỏ hơn p. Hãy nhập lại.")
    except ValueError:
        print("Giá trị không hợp lệ. Hãy nhập lại.")

# Tính khóa công khai h = g^a mod p
# alpha a p 
h = pow(g, a, p)

print("Khóa công khai (p, g, h):", (p, g, h)) #p alpha ya
print("Khóa bí mật a:", a)

# Nhập giá trị plaintext
while True:
    try:
        plaintext = int(input("Nhập văn bản cần mã hóa (số nguyên < p): "))
        if 0 <= plaintext < p:
            break
        else:
            print("Văn bản phải là số nguyên không âm nhỏ hơn p.")
    except ValueError:
        print("Giá trị không hợp lệ. Hãy nhập lại.")

# Tính k (số ngẫu nhiên)
while True:
    try:
        k = int(input("Nhập số ngẫu nhiên k (số nguyên dương < p): "))
        if 0 < k < p:
            break
        else:
            print("k phải là số nguyên dương nhỏ hơn p. Hãy nhập lại.")
    except ValueError:
        print("Giá trị không hợp lệ. Hãy nhập lại.")

# for a in 
# Tính c1 và c2
c1 = pow(g, k, p)
# tinh k to
c2 = (pow(h, k, p) * plaintext) % p

ciphertext = (c1, c2)

print("Văn bản mã hóa:", ciphertext)

# Tính s = c1^a mod p
#tinh k cua giai ma
s = pow(c1, a, p)

# Tính nghịch đảo modulo của s
s_inverse = mod_inverse(s, p)

# Tính văn bản gốc
decrypted_text = (c2 * s_inverse) % p

print("Văn bản đã giải mã:", decrypted_text)