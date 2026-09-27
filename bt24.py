s = input("Nhập một xâu ký tự: ")

so = 0
in_hoa = 0
in_thuong = 0
dac_biet = 0

for ch in s:
    if ch.isdigit():
        so += 1
    elif ch.isupper():
        in_hoa += 1
    elif ch.islower():
        in_thuong += 1
    else:
        dac_biet += 1

print(f"Số lượng ký tự số: {so}")
print(f"Số lượng chữ cái in hoa: {in_hoa}")
print(f"Số lượng chữ cái thường: {in_thuong}")
print(f"Số lượng ký tự đặc biệt: {dac_biet}")