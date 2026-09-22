import math
print("--- KIỂM TRA ĐIỂM M THUỘC HÌNH TRÒN ---")
x = float(input("Nhập tọa độ x của điểm M: "))
y = float(input("Nhập tọa độ y của điểm M: "))
a = float(input("Nhập tọa độ a của tâm I: "))
b = float(input("Nhập tọa độ b của tâm I: "))
R = float(input("Nhập bán kính R: "))

# khoảng cách từ M đến tâm I
d = math.sqrt(((x - a) ** 2) +((y - b) ** 2))

# Kiểm tra điều kiện (<= R^2)
ket_qua = d <= R
if ket_qua =d<=R:

print(ket_qua)
