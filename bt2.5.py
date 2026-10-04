import random
taphop1=[]
taphop2=[]
n=random.randint(1,10)
for i in range(10):
    taphop1.append(random.randint(1,10))
    taphop2.append(random.randint(1,10))
print(taphop1)
print(taphop2)
# tìm giao của hai tập hợp và loại các phần tử đó ra lhoir tập hợp thứ nhất
giao = []  # Khởi tạo là một list (danh sách)

for x in taphop1:
    if x in taphop2 and x not in giao:
        giao.append(x)
for x in giao:
    taphop1.remove(x)
print(giao)
print(taphop1)
print(taphop2)
for x in taphop2:
    # Dùng while để xóa tất cả các lần xuất hiện của x trong list1 (nếu có)
    while x in taphop1:
        taphop1.remove(x)
print("giao:", giao)
print("taphop1:", taphop1)
print("taphop2:", taphop2)
print("taphop1 sau khi xóa trực tiếp các phần tử trùng với taphop2:", taphop1)
la_tap_con = True
for x in taphop1:
    # Kiểm tra xem phần tử x có xuất hiện trong taphop2 hay không
    tim_thay = False
    for y in taphop2:
        if x == y:
            tim_thay = True
            break

    # Nếu có bất kỳ phần tử nào của taphop1 không có trong taphop2 thì không phải tập con
    if not tim_thay:
        la_tap_con = False
        break

print("b) th1 có là tập con của th2 không?", la_tap_con)
hop = []

# Bước 1: Đưa toàn bộ phần tử của th1 vào danh sách 'hop'
for x in taphop1:
    hop.append(x)

# Bước 2: Duyệt qua từng phần tử của th2
for x in taphop2:
    # Kiểm tra xem x đã có trong 'hop' chưa
    da_co = False
    for y in hop:
        if x == y:
            da_co = True
            break

    # Nếu chưa có thì mới thêm vào (để tránh bị lặp lại các số giống nhau)
    if not da_co:
        hop.append(x)

print("c) Hợp của hai danh sách :", hop)