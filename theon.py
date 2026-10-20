# 1. Nhập số lượng học sinh n (0 < n < 10)
n = int(input("Nhập số lượng học sinh n (0 < n < 10): "))

danh_sach_diem = []

# 2. Dùng vòng lặp for để nhập lần lượt điểm của từng học sinh
print(f"\n--- NHẬP ĐIỂM CHO {n} HỌC SINH ---")
for i in range(1, n + 1):
    diem = float(input(f"Nhập điểm của học sinh thứ {i}: "))
    danh_sach_diem.append(diem)

# 3. Tính điểm trung bình (TB) của cả lớp và làm tròn 2 chữ số
tong_diem = sum(danh_sach_diem)
diem_tb_lop = round(tong_diem / n, 2)

# 4. Đếm số lượng học sinh theo từng loại học lực
# - Giỏi: điểm >= 8.0
# - Khá: 6.5 <= điểm < 8.0
# - Trung bình: 5.0 <= điểm < 6.5
# - Yếu: điểm < 5.0
so_luong_gioi = 0
so_luong_kha = 0
so_luong_tb = 0
so_luong_yeu = 0

for diem in danh_sach_diem:
    if diem >= 8.0:
        so_luong_gioi += 1
    elif diem >= 6.5:
        so_luong_kha += 1
    elif diem >= 5.0:
        so_luong_tb += 1
    else:
        so_luong_yeu += 1

# 5. In kết quả ra màn hình
print("\n--- KẾT QUẢ PHÂN LOẠI ---")
print(f"Danh sách điểm các học sinh: {danh_sach_diem}")
print(f"👉 Điểm trung bình cả lớp: {diem_tb_lop}")
print("👉 Thống kê học lực:")
print(f"   - Số học sinh Giỏi (>= 8.0): {so_luong_gioi}")
print(f"   - Số học sinh Khá (6.5 - 7.9): {so_luong_kha}")
print(f"   - Số học sinh Trung bình (5.0 - 6.4): {so_luong_tb}")
print(f"   - Số học sinh Yếu (< 5.0): {so_luong_yeu}")