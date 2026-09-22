s = input("Nhập vào một xâu ký tự: ")

# Sử dụng hàm join để nối các ký tự lại với dấu cách ở giữa
print(" \n".join(s)) #nói chung
print (*s,sep="-")# tách từng ký tự bừng dấu đặc biệt
print(" ".join(s)+"\n")
