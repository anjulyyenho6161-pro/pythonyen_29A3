# Nhập 3 cạnh từ bàn phím
a = float(input("Nhập cạnh a: "))
b = float(input("Nhập cạnh b: "))
c = float(input("Nhập cạnh c: "))

# 1. Kiểm tra điều kiện để là tam giác: các cạnh phải lớn hơn 0
# và tổng hai cạnh bất kỳ luôn lớn hơn cạnh còn lại
if a > 0 and b > 0 and c > 0 and (a + b > c) and (a + c > b) and (b + c > a):

    # 2. Kiểm tra tam giác đều (3 cạnh bằng nhau)
    if a == b == c:
        print("Đây là tam giác đều.")
    else:
        # Kiểm tra tam giác vuông (dùng sai số nhỏ 1e-9 để xử lý số thực)
        is_vuong = (
                abs(a ** 2 + b ** 2 - c ** 2) < 1e-9 or#
                abs(a ** 2 + c ** 2 - b ** 2) < 1e-9 or
                abs(b ** 2 + c ** 2 - a ** 2) < 1e-9
        )#1e-9:giá trị tuyệt đối của hiệu nhỏ hơn một số vô cùng 0.000000001  kết quả  4.000000000000001 == 4 bị báo là sai.

        # Kiểm tra tam giác cân (có 2 cạnh bằng nhau)
        is_can = (a == b) or (b == c) or (a == c)

        # Phân loại dựa trên kết hợp vuông và cân
        if is_vuong and is_can:
            print("Đây là tam giác vuông cân.")
        elif is_vuong:
            print("Đây là tam giác vuông.")
        elif is_can:
            print("Đây là tam giác cân.")
        else:
            print("Đây là tam giác thường.")
else:
    print("Ba số vừa nhập không phải là bộ ba cạnh của một tam giác!")