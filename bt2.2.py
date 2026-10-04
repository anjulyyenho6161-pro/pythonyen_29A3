import random
# Cách 1: Dùng List Comprehension (ngắn gọn)
n=[random.randint(1, 100)
       for i in range(10)]
print("Danh sách ngẫu nhiên:", n)

# Cách 2: Dùng vòng lặp for thông thường
a = []
for i in range(10):
    gia_tri = random.randint(1, 100) # Sinh số nguyên ngẫu nhiên
    a.append(gia_tri)

print("Danh sách sau khi dùng vòng lặp:", a)
sodaxoa=a.pop(4)
print(a)
a.insert(2,sodaxoa)
print(a)
a.extend([sodaxoa])
print(a)
a.append(sodaxoa)
print(a)