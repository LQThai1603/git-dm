import numpy as np     # pip3 install numpy
from egcd import egcd  # python -m pip install egcd
import math

alphabet = "abcdefghijklmnopqrstuvwxyz"

letter_to_index = dict(zip(alphabet, range(len(alphabet))))
index_to_letter = dict(zip(range(len(alphabet)), alphabet))


def matrix_mod_inv(matrix, modulus): # tính ma trận nghịch đảo theo modun

    det = int(np.round(np.linalg.det(matrix)))  # tính định thức bằng hàm của numpy
    det_inv = egcd(det, modulus)[1] % modulus  # tính theo euclid mở rộng 
    matrix_modulus_inv = (det_inv * np.round(det * np.linalg.inv(matrix)).astype(int) % modulus)  

    return matrix_modulus_inv


def encrypt(message, K):
    encrypted = ""
    message_in_numbers = []

    for letter in message.lower():
        message_in_numbers.append(letter_to_index[letter])

    split_P = [ #  P được chia thành các khối có kích thước bằng số hàng của ma trận khóa K
        message_in_numbers[i: i + int(K.shape[0])]
        for i in range(0, len(message_in_numbers), int(K.shape[0]))
    ]

    for P in split_P: 
        P = np.transpose(np.asarray(P))[:, np.newaxis] # cd P thành ma trận cột

        while P.shape[0] != K.shape[0]:
            P = np.append(P, letter_to_index[" "])[:, np.newaxis]

        numbers = np.dot(K, P) % len(alphabet)
        n = numbers.shape[0] 

        for idx in range(n):
            number = int(numbers[idx, 0])
            encrypted += index_to_letter[number]

    return encrypted


def decrypt(cipher, Kinv):
    decrypted = ""
    cipher_in_numbers = []

    for letter in cipher:
        cipher_in_numbers.append(letter_to_index[letter])

    split_C = [
        cipher_in_numbers[i: i + int(Kinv.shape[0])]
        for i in range(0, len(cipher_in_numbers), int(Kinv.shape[0]))
    ]

    for C in split_C:
        C = np.transpose(np.asarray(C))[:, np.newaxis]
        numbers = np.dot(Kinv, C) % len(alphabet)
        n = numbers.shape[0]

        for idx in range(n):
            number = int(numbers[idx, 0])
            decrypted += index_to_letter[number]

    return decrypted




#Main

while 1:
        key = input("Nhập khóa: ").upper()
        if math.sqrt(len(key)).is_integer():
            do_dai_khoa = len(key)
            kich_thuoc_ma_tran = int(do_dai_khoa**0.5)
            ma_tran = np.zeros((kich_thuoc_ma_tran, kich_thuoc_ma_tran), dtype=int)

            for i in range(kich_thuoc_ma_tran):
                for j in range(kich_thuoc_ma_tran):
                    ma_tran[i, j] = (ord(key[i * kich_thuoc_ma_tran + j]) - ord('A'))

            det = int(np.round(np.linalg.det(ma_tran)))
            # print("Định thức ma trận:", det)  
            det_inv = egcd(det, 26)[1] % 26  # dựa vào moduls nghịch đảo để xét nếu khác 1 thì thỏa mãn
            print("Modulus nghịch đảo: ", det_inv)

            if det_inv != 1:
                matrix_modulus_inv = (det_inv * np.round(det * np.linalg.inv(ma_tran)).astype(int) % 26)
                print("Ma trận nghịch đảo: \n", matrix_modulus_inv)
                print("Ma trận vuông dựa trên chuỗi:")
                for i in range(kich_thuoc_ma_tran):
                    for j in range(kich_thuoc_ma_tran):
                        print(ma_tran[i, j], end=" ")
                    print()
                break
            else:
                print("Khóa không thỏa mãn điều kiện. Vui lòng nhập lại.")    
        else:
            print("Khóa không thỏa mãn điều kiện. Vui lòng nhập lại.")

   
while 1:
        message = input("Nhập chuỗi cần mã hóa: ")
        if len(message) % kich_thuoc_ma_tran == 0:
            break
        else:
            print("P không thỏa mãn điều kiện, nhập lại")

Kinv = matrix_mod_inv(ma_tran, len(alphabet))

encrypted_message = encrypt(message, ma_tran)   
decrypted_message = decrypt(encrypted_message, Kinv)

if(message.isupper()):
    print("Mã hóa: " + encrypted_message.upper())
    print("Giải mã: " + decrypted_message.upper())
else:
    print("Mã hóa: " + encrypted_message)
    print("Giải mã: " + decrypted_message)


