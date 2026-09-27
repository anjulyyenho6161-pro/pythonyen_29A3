s = input("Nhập xâu ký tự chính: ")
sub = input("Nhập chuỗi con cần tìm: ")

# Sử dụng hàm count() để đếm số lần xuất hiện của chuỗi con
so_lan = s.count(sub)
print(f"Số lần xuất hiện của '{sub}' trong xâu là: {so_lan}")