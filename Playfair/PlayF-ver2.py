import string
# Sinh khoa
def key_matrix_generation(key):
    atoz = string.ascii_lowercase.replace('j', '.') #Doi j = .

    key_matrix = [ '' for i in range(5) ] # tao ma tran 5x5

    i = 0
    j = 0

    for c in key: 
        if c in atoz: # kiem tra xem co trong bang chu cai va thay doi khong
            key_matrix[i] += c # them tu khoa vao ma tran

            atoz = atoz.replace(c, '.') # sau khi them thi bien chu cai do thanh dau . de khong them lai lan nua

            j += 1
            # kiem tra do dai ma row ma tran neu du dai chuyen sang hang khac
            if j > 4:
                i += 1
                j = 0

    # them cac chu cai con lai vao ma tran
    for c in atoz:
        if c != '.':
            key_matrix[i] += c

            j += 1
            if j > 4:
                i += 1
                j = 0
    return key_matrix

def encrypt(plain_Text):
    plain_Text_Pairs = []
    cipher_Text_Pairs = []

    #1
    i = 0
    while i < len(plain_Text):
        a = plain_Text[i]
        b = ''
        if (i + 1) == len(plain_Text):
            b = 'x'
        else:
            b = plain_Text[i + 1]

        if a != b:
            plain_Text_Pairs.append(a + b)
            i += 2
        else:
            plain_Text_Pairs.append(a + 'x')
            i += 1
    print(plain_Text_Pairs)

    #2
    for pair in plain_Text_Pairs:
        applied_rule = False
        for row in key_matrix:
            if pair[0] in row and pair[1] in row:
                j0 = row.find(pair[0])
                j1 = row.find(pair[1])

                cipher_Text_Pair = row[(j0 + 1) % 5] + row[(j1 + 1) % 5]
                cipher_Text_Pairs.append(cipher_Text_Pair)
                applied_rule = True

        if applied_rule:
            continue

        #3
        for j in range(5):
            col = "".join([key_matrix[i][j] for i in range(5)])
            if pair[0] in col and pair[1] in col:
                i0 = col.find(pair[0])
                i1 = col.find(pair[1])

                cipher_Text_Pair = col[(i0 + 1) % 5] + col[(i1 + 1) % 5]
                cipher_Text_Pairs.append(cipher_Text_Pair)
                applied_rule = True

        if applied_rule:
            continue

        #4
        i0 = 0
        i1 = 0
        j0 = 0
        j1 = 0
        for i in range(5):
            row = key_matrix[i]
            if pair[0] in row:
                i0 = i
                j0 = row.find(pair[0])

            if pair[1] in row:
                i1 = i
                j1 = row.find(pair[1])

        cipher_Text_Pair = key_matrix[i0][j1] + key_matrix[i1][j0]        

        cipher_Text_Pairs.append(cipher_Text_Pair)
    return cipher_Text_Pairs

def decrypt(cipher_Text):
    plain_Text_Pairs = []
    cipher_Text_Pairs = []
    #1
    i = 0
    while i < len(cipher_Text):
        a = cipher_Text[i]
        b = cipher_Text[i + 1]

        cipher_Text_Pairs.append(a + b)
        i += 2
    print(cipher_Text_Pairs)

    #2
    for pair in cipher_Text_Pairs:
        applied_rule = False
        for row in key_matrix:
            if pair[0] in row and pair[1] in row:
                j0 = row.find(pair[0])
                j1 = row.find(pair[1])

                plain_Text_Pair = row[(j0 + 4) % 5] + row[(j1 + 4) % 5]
                plain_Text_Pairs.append(plain_Text_Pair)
                applied_rule = True

        if applied_rule:
            continue

        #3
        for j in range(5):
            col = "".join([key_matrix[i][j] for i in range(5)])
            if pair[0] in col and pair[1] in col:
                i0 = col.find(pair[0])
                i1 = col.find(pair[1])

                plain_Text_Pair = col[(i0 + 4) % 5] + col[(i1 + 4) % 5]
                plain_Text_Pairs.append(plain_Text_Pair)
                applied_rule = True

        if applied_rule:
            continue

        #4
        i0 = 0
        i1 = 0
        j0 = 0
        j1 = 0
        for i in range(5):
            row = key_matrix[i]
            if pair[0] in row:
                i0 = i
                j0 = row.find(pair[0])

            if pair[1] in row:
                i1 = i
                j1 = row.find(pair[1])

        plain_Text_Pair = key_matrix[i0][j1] + key_matrix[i1][j0]        

        plain_Text_Pairs.append(plain_Text_Pair)
    return plain_Text_Pairs


# Main
# key = input("nhập khóa ma trận: ")
# key = key.lower()
# while 1:
#     check = True
#     for j in key:
#         if j.isalpha() == False:
#             print("mã chỉ có thể là các chữ cái")
#             check = False
#             break
#     if check:
#         break
while True:
    key = input("Nhập key: ")
    key = key.lower()
    if len(key) < 1 or not key.isalpha():
        print("Key không hợp lệ, Vui lòng nhập lại")
        continue
    break
            

key_matrix = key_matrix_generation(key)
print(key_matrix)

# plain_Text = "communicate"

while True:
    plain_Text = input("nhập chuỗi plain_text: ")
    
    if len(plain_Text) < 1 or not plain_Text.isalpha():
        print("Chuỗi cần mã hóa không hợp lệ, Vui lòng nhập lại")
        continue
    break

check = []
for c in plain_Text:
    if(c.isupper()):
        check.append(1)
    else:
        check.append(0)

plain_Text = plain_Text.lower()

cipher_Text1 = "" + "".join(encrypt(plain_Text))
if(len(check) != len(cipher_Text1)):
    check.append(0)
c1 = ""

for index, value in enumerate(cipher_Text1):
    if check[index] == 1:
        c1 +=value.upper()
    else:
        c1 += value

print("cipher_text: " + c1)

cipher_Text = input("nhập chuỗi cipher_text: ")

cipher_Text = cipher_Text.lower()   

plain_Text1 = ""

plain_Text1 += "".join(decrypt(cipher_Text))

print(plain_Text1)

p1 = ""
i = 0
j = 0
while i < len(check):
    if(i>0 and i<(len(check)-1) and plain_Text1[i-1] == plain_Text1[i+1] and plain_Text1[i] == 'x'):
        i+=1
        j=i+1
        p1 += 'x'
    elif j == len(check):
        break
    elif check[i] == 1:
        p1 += plain_Text1[j].upper()
        j+=1
        i+=1
    else:
        p1 += plain_Text1[j]
        j+=1
        i+=1

if(len(plain_Text) < len(p1)):
    p1 = p1[:-1]
print("plain_Text: " + p1)