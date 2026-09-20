# Nhập năm từ bàn phím

nam = int(input("Nhập vào một năm cần kiểm tra: "))
# Quy tắc năm nhuận: Chia hết cho 4 nhưng không chia hết cho 100,
# hoặc chia hết cho 400
if (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0):
        print(f"Năm {nam} là năm nhuận.")
else:
        print(f"Năm {nam} không phải là năm nhuận.")
