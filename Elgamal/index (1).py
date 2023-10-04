import math

# Hàm kiểm tra SNT
def prime_checker(num):
	# Kiểm tra P có là số nguyên tố hay không
    if num == 2:
        return 1
    if num < 2 or num % 2 == 0:
        return -1
    for n in range(3, int(num**0.5)+2, 2):
        if num % n == 0:
            return -1
    return 1

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def euler_phi(n):
    phi = 0
    for i in range(1, n):
        if gcd(i, n) == 1:
            phi += 1
    return phi

def coprime_numbers_with_n(n):
    coprimes = []
    for i in range(1, n):
        if gcd(i, n) == 1:
            coprimes.append(i)
    return coprimes

def is_primitive_root(a, n, phi):
    factors = prime_factors(phi)
    for p in factors:
        if pow(a, phi // p, n) == 1:
            return False
    return True
	
def prime_factors(n):
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n**0.5)+1, 2):
        while n % i == 0:
            factors.append(i)
            n = n // i
    if n > 2:
        factors.append(n)
    return set(factors)

def select_primitive_root(primitive_roots):
    while True:
        for i, root in enumerate(primitive_roots):
            print(f"{i + 1}. {root}")
        
        choice = input("Chọn một căn nguyên thủy (1, 2, ...) hoặc nhấn Enter để thoát: ")
        if choice == "":
            return None  # Người dùng không chọn gì, trả về None
        try:
            index = int(choice) - 1
            if 0 <= index < len(primitive_roots):
                return primitive_roots[index]  # Trả về căn nguyên thủy được chọn
            else:
                print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")
        except ValueError:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")

while 1:
	p = int(input("Nhập p : "))
	if prime_checker(p) == -1:
		print("{p} không phải là SNT, Vui lòng nhập lại!")
		continue
	break


phi = euler_phi(p)
print(f"Số các số nguyên tố cùng nhau với {p} là {phi}:")
coprimes = coprime_numbers_with_n(p)
print(coprimes)

primitive_roots = []
for a in coprimes:
    if is_primitive_root(a, p, phi):
        primitive_roots.append(a)

print(f"Các căn nguyên thủy của {p} là: ")
print(primitive_roots)

selected_root = select_primitive_root(primitive_roots)
if selected_root is not None:
    print(f"Bạn đã chọn căn nguyên thủy: {selected_root}")
else:
    print("Bạn đã thoát chương trình.")
    
alpha = selected_root

# Private Keys
while 1:
    x1, x2 = int(input("Enter The Private Key Of User 1 : ")), int(
	input("Enter The Private Key Of User 2 : "))
    if x1 > p-1 or x2 > p-1:
        print(f"Khóa riêng tư của cả hai người dùng phải nhỏ hơn {p-1}, Vui lòng nhập lại!")
        continue
    break

y1, y2 = pow(alpha, x1) % p, pow(alpha, x2) % p
print("Pulic Key 1: ", (p, alpha, y1))
print("Private Key 1: ", x1)
print("Pulic Key 2: ", (p, alpha, y2))
print("Private Key 2: ", x2)

while 1:
    P = int(input("Nhập P(phần tử rõ) : "))
    if P > p:
        print(f"Số vừa nhập (phần tử rõ) phải nhỏ hơn {p}, Vui lòng nhập lại!")
        continue
    break

while 1:
    k = int(input("Nhập k(số nguyên ngẫu nhiên) : "))
    if k <= 0 or k >= p-1:
        print(f"Số vừa nhập (phần tử rõ) phải <= {p - 1} và >= 0, Vui lòng nhập lại!")
        continue
    break


K = pow(y1, k) % p
C1 = pow(alpha, k) % p
C2 = (K * P) % p

print("--Mã hóa--")
print("Bản mã là: ", (C1, C2))

print("--Giải mã--")

# Hàm eculid mở rộng (gcd: UCLN, y, x là hệ số Bezout)
def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    else:
        gcd, x, y = extended_gcd(b, a % b)
        return gcd, y, x - (a // b) * y
    
    
K1 = pow(C1, x1) % p
gcd, x_gcd, y_gcd = extended_gcd(K1, p)
if x_gcd < 0:
    x_gcd = x_gcd + p

# x_gcd = K^-1
P1 = (C2 * x_gcd) % p
print("Bản rõ là: ", P1)