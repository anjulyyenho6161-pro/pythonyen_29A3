# 1. Nhập số lượng học sinh n (0 < n < 10)
n = int(input("Nhập số lượng học sinh n (0 < n < 10): "))

print(f"Chương trình mặc định với n = {n} từ.")

# Nhập chuỗi và tự động tách từ
while True:
    chuoi = input(f"Nhập chuỗi gồm đúng {n} từ (cách nhau bằng khoảng trắng): ").strip()
    danh_sach_tu = chuoi.split()

    if len(danh_sach_tu) == n:
        break
    else:
        print(f"⚠️ Bạn vừa nhập {len(danh_sach_tu)} từ. Yêu cầu phải nhập đúng {n} từ! Vui lòng nhập lại.")

print("\n--- KẾT QUẢ PHÂN TÍCH ---")
print(f"Danh sách các từ: {danh_sach_tu}")

# 1. Đếm số lượng từ có độ dài >= 5 ký tự
dem_tu_dai = 0
for tu in danh_sach_tu:
    if len(tu) >= 5:
        dem_tu_dai += 1
print(f"👉 Số lượng từ có độ dài >= 5 ký tự : {n}: {dem_tu_dai}")

# 2. Tìm độ dài lớn nhất và vị trí
max_len = 0
for tu in danh_sach_tu:
    if len(tu) > max_len:
        max_len = len(tu)

danh_sach_max = []
for vi_tri, tu in enumerate(danh_sach_tu):
    if len(tu) == max_len:
        danh_sach_max.append((vi_tri + 1, tu))

print(f"👉 Độ dài lớn nhất trong các từ là: {max_len} ký tự")
print("👉 Từ dài nhất xuất hiện tại vị trí:")
for vt, tu in danh_sach_max:
    print(f"   - Từ '{tu}' nằm ở vị trí thứ {vt}")
