import math
while True:# tạo một vòng lặp Chương trình sẽ lặp đi lặp lại các lệnh bên trong cho đến khi gặp lệnh break.
    m = int(input("Nhập số nguyên dương m: "))
    n = int(input("Nhập số nguyên dương n: "))
    # Phép thử kiểm tra các điều kiện: m > 0, n > 0 và m > n
    if m > 0 and n > 0 and m > n:
        break  # Điều kiện đúng -> Thoát khỏi vòng lặp
    else:#điều kiện sai -> thực hiện lệnh in dòng thông báo của print
        print(" Yêu cầu m > n. Vui lòng nhập lại!\n")

phan_nguyen=m//n   #tính phần nguyên
phan_du=m%n    #tính phần dư

#in kết quả ra màn hình
print ("phần nguyên của ",m,"chia",n,"là:",phan_nguyen)
print ("phần dư của ",m,"chia",n,"là:",phan_du)

'''
Bước 1: Khởi tạo vòng lặp vô hạn (while True) để liên tục yêu cầu người dùng nhập liệu cho đến khi nhận được dữ liệu hợp lệ.
Bước 2: Nhập giá trị số nguyên cho hai biến m và n từ bàn phím.
Bước 3: Kiểm tra biểu thức điều kiện hợp lệ: m > 0 and n > 0 and m > n.
Nếu điều kiện đúng, thực hiện lệnh break để chấm dứt vòng lặp và tiếp tục thực hiện các câu lệnh bên ngoài vòng lặp.
Nếu điều kiện sai, hiển thị thông báo lỗi "Yêu cầu m > n. Vui lòng nhập lại!" và quay lại Bước 2 để nhập lại từ đầu.'''