n = int(input("Nhập vào số n: "))
so_chan = 0
so_le = 0
i = 1

''' while i <= n:
    if i % 2 == 0:
        so_chan = so_chan + i ** 2  # Cộng dồn số chẵn
    else:
        so_le = so_le + i ** 2  # Cộng dồn số lẻ

    i = i + 1

print(f"Tổng bình phương các số chẵn từ 1 đến {n}: {so_chan}")
print(f"Tổng bình phương các số lẻ từ 1 đến {n}: {so_le}") '''

for i in range(1,n+1,2):
    if i%2 !=0:
     so_le=so_le+(i*i)
print(f"Tổng bình phương các số lẻ từ 1 đến {n}: {so_le}")

for i in range(1,n+1,2):
     so_le=so_le+(i*i)
print(f"Tổng bình phương các số lẻ từ 1 đến {n}: {so_le}")