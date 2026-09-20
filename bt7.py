import math

# Nhập giá trị x và y từ bàn phím
# Lưu ý: Các hàm sin và cos trong Python tính theo đơn vị radian.
# Nếu bạn muốn nhập x theo độ (degrees), hãy đổi thành: x = math.radians(float(input(...)))
x = float(input("Nhập giá trị x (radian): "))
y = float(input("Nhập giá trị y: "))

# Tính giá trị biểu thức f(x, y) = 3*sin(x) + 4*cos(x)
f = 3 * math.sin(x) + 4 * math.cos(x)

# In kết quả ra màn hình
print(f"Giá trị của biểu thức f(x, y) tại x = {x}, y = {y} là: {f}")