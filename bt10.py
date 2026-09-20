a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))

# Sửa lỗi ở dòng này (dùng f-string)
print(f"PHƯƠNG TRÌNH BẬC NHẤT: {a}x + {b} = 0")

if a == 0:
    if b == 0:
        print("Phương trình có vô số nghiệm.")
    else:
        print("Phương trình vô nghiệm.")
else:
    x = -b / a
    print(f"Phương trình có nghiệm duy nhất: x = {x}")
