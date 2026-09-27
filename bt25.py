n= input("Nhập vào một số nguyên: ")

# Xử lý loại bỏ dấu trừ nếu là số âm để tính tổng các chữ số
n1 = n.lstrip('-')
'''n1 = str(abs(n))'''
tong = 0
ds = []

for ch in n1:
    if ch.isdigit():
        tong += int(ch)# đưa sôs trong ds từ "1" sang 1 để tính toán
        ds.append(ch)

# In kết quả theo đúng định dạng ví dụ
print(f"S = " + " + ".join(ds) + f" = {tong}")