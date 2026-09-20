# Bước 1: Nhập nhiệt độ C từ bàn phím
celsius = float(input("Nhập nhiệt độ Celsius: "))

# Bước 2: Tính nhiệt độ Kelvin
kelvin = celsius + 273.15

# Bước 3: In kết quả ra màn hình
print(celsius, "độ C bằng", kelvin, "K")

'''Dòng 1: celsius = float(input("Nhập nhiệt độ Celsius: ")
input : Hiện dòng chữ thông báo 
float : Biến văn bản người dùng vừa gõ thành số thập phân (để có thể thực hiện phép cộng toán học).
celsius =: Lưu con số đó vào tên là celsius.

 Dòng 2: kelvin = celsius + 273.15
 Lấy con số đang đc gán trong 'celsius' cộng thêm 273.15 sau đó, lưu kết quả vừa tính được vào một tên mới là kelvin.
 
 Dòng 3: print(celsius, "độ C bằng", kelvin, "K")
 Hàm print() dùng để hiển thị dữ liệu ra màn hình.
 Các thành phần cách nhau bởi dấu phẩy sẽ được in ra nối tiếp nhau  '''
