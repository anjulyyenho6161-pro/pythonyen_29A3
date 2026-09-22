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
if d<R:
  print("điểm M nằm trong hình tròn")
elif d=R:
  print("điểm m nằm trên hình tròn")
else:
  print(" điểm m nằm ngoài hình tròn")

print(ket_qua)
