n = int(input("Nhập số nguyên dương n: "))

'''# Lọc ra các số nguyên tố nhỏ hơn n bằng list comprehension
danh_sach_snt = [
    str(i) for i in range(2, n) 
    if all(i % j != 0 for j in range(2, int(i**0.5) + 1))
]

print(f"Có {len(danh_sach_snt)} số nguyên tố nhỏ hơn {n}.")
print("Các số đó là: " + ", ".join(danh_sach_snt))'''


if n <= 1:
    print(f"Không có số nguyên tố nào nhỏ hơn {n}.")
else:
    dem = 0
    danh_sach_snt = []

    # Duyệt từng số i từ 2 đến n - 1
    for i in range(2, n):
        la_snt = True

        # Kiểm tra xem i có phải là số nguyên tố không
        # Chỉ cần chạy vòng lặp từ 2 đến căn bậc hai của i
        for j in range(2, int(i ** 0.5) + 1):# (2,math.sqrt(i)) +1 để chạy luôn i 
            if i % j == 0:
                la_snt = False
                break  # Thoát vòng lặp ngay nếu phát hiện không phải số nguyên tố

        # Nếu i là số nguyên tố thì tăng biến đếm và lưu lại
        if la_snt:
            dem += 1
            danh_sach_snt.append(str(i))

    print(f"Có {dem} số nguyên tố nhỏ hơn {n}.")
    print("Các số đó là: " + ", ".join(danh_sach_snt))
