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

# Nhập số a và p
a = int(input("Nhập số a: "))
p = int(input("Nhập số p: "))

if is_primitive_root(a, p):
    print(f"{a} là căn nguyên thủy modulo {p}")
else:
    print(f"{a} không phải là căn nguyên thủy modulo {p}")
