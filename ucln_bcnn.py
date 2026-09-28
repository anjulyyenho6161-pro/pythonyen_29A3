import math

# Nhập hai số m và n từ bàn phím
m = int(input("Nhập số m: "))
n = int(input("Nhập số n: "))

'''# Tính ƯCLN bằng hàm math.gcd
ucln = math.gcd(m, n)

# Tính BCNN bằng hàm math.lcm (hoặc dùng công thức m * n // ucln)
bcnn = math.lcm(m, n)

# In kết quả ra màn hình
print(f"Ước chung lớn nhất (ƯCLN) của {m} và {n} là: {ucln}")
print(f"Bội chung nhỏ nhất (BCNN) của {m} và {n} là: {bcnn}")
while m!=0:
     du=m%n
     m=n
     n=du
ucln=m
bcnn=m*n//ucln'''

for i in range(1,m*n):
    if m %i==0 and n%i==0:
        ucln=i
print(ucln)
for i in range(1,m*n):
    if i%m==0 and n%i==0:
       bcnn=i
       break
print(bcnn)





