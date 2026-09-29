'''dsten=["yến ","linh","minh"]
print(dsten)
print(dsten[1])
print("IN DS THEO CON TRỎ ")
for ten in dsten:
    print(ten)
print(" IN THEO CHỈ SỐ ")
for i in range(0,len(dsten),1):
    print(dsten[i])'''
dsso=[]
n=int(input("nhập vào n phần tử"))
for i in range(1,n+1):
    ni=int(input(f"A[{i}]="))
    dsso.append(i)
print(dsso)
so_pt=len(dsso)
print(so_pt)
if so_pt>0:
    somax=max(dsso)
    print(f"số lớn nhất trong danh sách là:{somax}")
    somin=min(dsso)
    print(f"số nhỏ nhất trong danh sách là:{somin}")
    trungbinh=sum(dsso)//n
    print(f" trungbinh của các giá trị trong danh sách là:{trungbinh}")
else:
    print ("dsso là ds rỗng")
if so_pt > 0:
    # b) Tìm phần tử lớn nhất, nhỏ nhất và tính trung bình bằng vòng lặp
    phan_tu_max = dsso[0]
    phan_tu_min = dsso[0]
    tong_gia_tri = 0

    for x in dsso:
        if x > phan_tu_max:
            phan_tu_max = x
        if x < phan_tu_min:
            phan_tu_min = x
        tong_gia_tri += x

    trung_binh = tong_gia_tri / so_pt

    print(f"b) Phần tử lớn nhất: {phan_tu_max}")
    print(f"   Phần tử nhỏ nhất: {phan_tu_min}")
    print(f"   Trung bình cộng các giá trị: {trung_binh:.2f}")
else:
    print("b) Danh sách rỗng.")

# c) Tính tổng các số chẵn, tổng các số lẻ trong danh sách
tong_chan = sum(x for x in dsso if x % 2 == 0)
tong_le = sum(x for x in dsso if x % 2 != 0)
print(f"c) Tổng các số chẵn: {tong_chan}")
print(f"   Tổng các số lẻ: {tong_le}")

# c) Tính tổng các số chẵn, tổng các số lẻ dùng vòng lặp
tchan = 0
tle = 0

for i in dsso:
    if i % 2 == 0:
        tchan += i
    else:
        tle += i

print(f"c) Tổng các số chẵn: {tchan}")
print(f"   Tổng các số lẻ: {tle}")








# d) Tạo 2 Tuple: một chứa các số dương, một chứa các số âm
# (Lưu ý: Số 0 không phải là số dương cũng không phải số âm)
tuple_duong = tuple(x for x in dsso if x > 0)
tuple_am = tuple(x for x in dsso if x < 0)
print(f"d) Tuple các số dương: {tuple_duong}")
print(f"   Tuple các số âm: {tuple_am}")
# d) Tạo 2 Tuple: số dương và số âm bằng vòng lặp duyệt qua danh sách
danh_sach_duong = []
danh_sach_am = []

for x in dsso:
    if x > 0:
        danh_sach_duong.append(x)
    elif x < 0:
        danh_sach_am.append(x)

tuple_duong = tuple(danh_sach_duong)
tuple_am = tuple(danh_sach_am)

print(f"d) Tuple các số dương: {tuple_duong}")
print(f"   Tuple các số âm: {tuple_am}")

# Khởi tạo danh sách lưu trữ (giá trị, vị trí)
dschan = []
dsle = []

# Sử dụng vòng lặp và enumerate để lấy cả phần tử (x) và vị trí (index)
for index, x in enumerate(dsso):
    if x % 2 == 0:
        dschan.append((x, index))
    else:
        dsle.append((x, index))

# --- IN KẾT QUẢ SỐ CHẴN ---
print(f"\n1. Các số chẵn (Tổng số lượng: {len(dschan)}):")
for gia_tri, vi_tri in dschan:
    print(f"   - Số chẵn: {gia_tri} | Vị trí (index): {vi_tri}")

# --- IN KẾT QUẢ SỐ LẺ ---
print(f"\n2. Các số lẻ (Tổng số lượng: {len(dsle)}):")
for gia_tri, vi_tri in dsle:
    print(f"   - Số lẻ: {gia_tri} | Vị trí (index): {vi_tri}")