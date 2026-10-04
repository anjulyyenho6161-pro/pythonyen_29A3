import random

# Khởi tạo n là một số nguyên ngẫu nhiên ban đầu
n = [random.randint(1, 100)]

for i in range(10):
  n.append(random.randint(1, 10))
print(n)
n.reverse()
print(n)
'''import random

# Khởi tạo một danh sách rỗng để chứa các phần tử ngẫu nhiên
danh_sach = []

# Khởi tạo một biến cộng dồn (ví dụ bắt đầu từ 0 hoặc một số ngẫu nhiên)
tong_cong_don = 0

print("--- VÒNG LẶP CHẠY 10 LẦN ---")
for i in range(10):
    # 1. Sinh một số nguyên ngẫu nhiên từ 1 đến 100
    so_ngau_nhien = random.randint(1, 100)
    
    # 2. Thêm số ngẫu nhiên đó vào danh sách (dùng .append)
    danh_sach.append(so_ngau_nhien)
    
    # 3. Cộng dồn giá trị vào biến tong_cong_don
    tong_cong_don += so_ngau_nhien
    
    # In ra kết quả của từng bước lặp
    print(f"Lần {i+1}: Thêm số {so_ngau_nhien} | Tổng cộng dồn hiện tại là: {tong_cong_don}")

# Kết quả cuối cùng
print("\n--- KẾT QUẢ CUỐI CÙNG ---")
print("Danh sách hoàn chỉnh (có ít nhất 10 phần tử):", danh_sach)
print("Tổng giá trị cộng dồn của tất cả các phần tử trong danh sách:", tong_cong_don)'''