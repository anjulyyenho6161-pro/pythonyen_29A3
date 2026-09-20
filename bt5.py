# Nhập 3 số nguyên dương a, b, h từ bàn phím
a = int(input("Nhập độ dài đáy lớn a: "))
b = int(input("Nhập độ dài đáy bé b: "))
h = int(input("Nhập chiều cao h: "))

# Tính diện tích hình thang
dien_tich = (a + b) * h / 2

# In kết quả ra màn hình
print(f"Diện tích hình thang là: {dien_tich}")