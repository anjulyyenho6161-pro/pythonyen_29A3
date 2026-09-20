import math

# Bước 1: Nhập bán kính từ bàn phím
r = float(input("Nhập bán kính hình tròn (r): "))

# Bước 2: Tính chu vi và diện tích
chu_vi = 2 * math.pi * r
dien_tich = math.pi * (r**2)

# Bước 3: In kết quả ra màn hình
print(f"Chu vi hình tròn là:, {chu_vi:.2f}")
print(f"Diện tích hình tròn là:,{dien_tich:.2f}")