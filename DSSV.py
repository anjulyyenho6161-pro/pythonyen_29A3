A=[6.5, 4.0, 9.0, 7.0, 3.5, 9.0, 6.0, 8.0]
dat=[]
khongdat=[]

B = []
max = A[0]
vtmax = [0]

# Duyệt qua từng phần tử và vị trí của danh sách A trong một vòng lặp duy nhất
for i in range(len(A)):
    diem = A[i]

    # 1 & 2. Đếm số sinh viên đạt và chưa đạt
    if diem >= 5:
        dat=dat + 1
    else:
        khongdat =khongdat + 1

    # 3. Tạo danh sách B chứa các điểm từ 7 trở lên
    if diem >= 7:
        B.append(diem)

    # 4 & 5 (Thử thách). Tìm điểm cao nhất và tất cả các vị trí xuất hiện của nó
    if diem > max:
        max = diem
        vtmax = [i]  # Tìm thấy điểm lớn hơn mới -> làm mới danh sách vị trí
    elif diem == max and i != 0:
        vtmax.append(i)  # Trùng với điểm cao nhất hiện tại -> bổ sung vị trí

# In kết quả ra màn hình
print(f"Số sinh viên >= 5: {dat}")
print(f"Số sinh viên < 5: {khongdat}")
print(f"Danh sách điểm >= 7: {B}")
print(f"Điểm cao nhất: {max}")
print(f"Vị trí điểm cao nhất: {vtmax}")