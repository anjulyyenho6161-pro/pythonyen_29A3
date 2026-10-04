import random
ds = []
# Vòng lặp chạy 10 lần để thêm 10 số ngẫu nhiên (từ 1 đến 10) vào danh sách ds
for i in range(10):
    ds.append(random.randint(1, 10))

print("Danh sách ngẫu nhiên vừa tạo là:", ds)

# a & b) Tạo dictionary đếm số lần xuất hiện của từng phần tử trong ds
myDictionary = {}
for item in ds:
    # Dùng .get(item, 0) để lấy số lần xuất hiện hiện tại (nếu chưa có thì mặc định là 0) rồi cộng thêm 1
    myDictionary[item] = myDictionary.get(item, 0) + 1

print("\nTừ điển thống kê số lần xuất hiện:")
print("myDictionary =", myDictionary)
for item in ds:
    # Kiểm tra xem item đã có trong dictionary chưa
    if item in myDictionary:
        myDictionary[item] += 1  # Nếu có rồi thì tăng số đếm lên 1
    else:
        myDictionary[item] = 1   # Nếu chưa có thì khởi tạo bằng 1

print("myDictionary =", myDictionary)