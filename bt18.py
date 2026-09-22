def dem_so_nguyen_to(n):
  count = 0
  print(f"Các số nguyên tố nhỏ hơn {n} là: ", end="")

  # Vòng lặp ngoài: duyệt các số từ 2 đến n-1
  for num in range(2, n):
  nguyento = True

    # Vòng lặp trong: kiểm tra tính nguyên tố của num
    for i in range(2, int(num**0.5) + 1):
      if num % i == 0:
       nguyento = False
        break  # Không phải số nguyên tố, thoát vòng lặp trong
    if nguyento:
      print(num, end=" ")
      count += 1
  return count
# --- Chương trình chính ---
n = 20  # Bạn có thể thay đổi giá trị của n tại đây (nếu n là số nguyên tố hoặc bất kỳ số nào)
ket_qua = dem_so_nguyen_to(n)
print(f"Tổng số lượng số nguyên tố nhỏ hơn {n} là: {ket_qua}")
