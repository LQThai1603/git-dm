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
        # for i, root in enumerate(primitive_roots):
        #     print(f"{i + 1}. {root}")
        
        choice = input("Chọn căn nguyên thủy thứ mấy hoặc nhấn Enter để thoát: ")
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


# Nhập vào từ bàn phím
while 1:
    P = input("Nhập P: ")
    if not P.isdigit():
        print("P phải là số nguyên tố. Vui lòng nhập lại: ")
        continue
    P = int(P)
    if prime_checker(P) == -1:
        print("P phải là số nguyên tố. Vui lòng nhập lại: ")
        continue
    break

phi = euler_phi(P)
print(f"Số các số nguyên tố cùng nhau với {P} là {phi}:")
coprimes = coprime_numbers_with_n(P)
print(coprimes)

primitive_roots = []
for a in coprimes:
    if is_primitive_root(a, P, phi):
        primitive_roots.append(a)

print(f"Các căn nguyên thủy của {P} là: ")
print(primitive_roots)

selected_root = select_primitive_root(primitive_roots)
if selected_root is not None:  # Trả về 1 giá trị khác khác None
    print(f"Bạn đã chọn căn nguyên thủy: {selected_root}")
else:
    print("Bạn đã thoát chương trình.")
    exit(None)
    
    
G = selected_root

# Private Keys
while 1:
    x1 = input("Enter The Private Key Of User 1: ")
    x2 = input("Enter The Private Key Of User 2: ")
    
    if not x1.isdigit() or not x2.isdigit():
        print("Khóa riêng tư của cả hai người dùng không hợp lệ. Vui lòng nhập lại.")
        continue
    
    x1 = int(x1)
    x2 = int(x2)
    
    if x1 > P or x2 > P:
        print(f"Khóa riêng tư của cả hai người dùng phải nhỏ hơn {P}, Vui lòng nhập lại!")
        continue
    break
    

# Tính khóa công khai
y1, y2 = pow(G, x1) % P, pow(G, x2) % P

# Tạo khóa bí mật
k1, k2 = pow(y2, x1) % P, pow(y1, x2) % P

print(f"\nKhóa công khai User 1 là:  {y1}\nKhóa công khai User 2 là: {y2}\n")

print(f"\nKhóa bí mật User 1 là: {k1}\nKhóa bí mật User 2 là: {k2}\n")

if k1 == k2:
	print("Trao đổi khóa thành công")
else:
	print("Trao đổi khóa không thành công")
