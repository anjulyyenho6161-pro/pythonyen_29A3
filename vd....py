class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class DSLK:
    def __init__(self):
        self.head = None

    def themcuoi(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        p = self.head
        while p.next is not None:
            p = p.next
        p.next = new_node

    # 📌 Hàm in danh sách (inds)
    def inds(self):
        p = self.head
        print("Danh sách DSLK: ", end="")
        while p is not None:
            print(p.data, end=" -> ")
            p = p.next
        print("None")

    # --- BÀI 5 & 10: TÌM ĐOẠN TĂNG LIÊN TIẾP DÀI NHẤT ---
    def tim_doan_tang_dai_nhat(self):
        if self.head is None:
            print("Danh sách trống!")
            return

        max_len = 1
        curr_len = 1
        best_start = self.head.data
        best_end = self.head.data
        curr_start = self.head.data

        prev_val = self.head.data
        p = self.head.next

        while p is not None:
            if p.data > prev_val:
                curr_len += 1
            else:
                curr_len = 1
                curr_start = p.data

            if curr_len > max_len:
                max_len = curr_len
                best_start = curr_start
                best_end = p.data

            prev_val = p.data
            p = p.next

        print(f"👉 [Bài 5 & 10] Đoạn tăng dài nhất có độ dài = {max_len} (Từ {best_start} đến {best_end})")

    # --- BÀI 6: TÌM CẶP PHẦN TỬ CÓ TỔNG BẰNG K ---
    def tim_cap_tong_bang_k(self, K):
        print(f"👉 [Bài 6] Các cặp phần tử có tổng bằng {K}:")
        p1 = self.head
        while p1 is not None:
            p2 = p1.next
            while p2 is not None:
                if p1.data + p2.data == K:
                    print(f"   - Cặp ({p1.data}, {p2.data})")
                p2 = p2.next
            p1 = p1.next

    # --- BÀI 7 & 9: PHÂN TÍCH CHỮ SỐ, ĐỐI XỨNG & ARMSTRONG ---
    def phan_tich_so_nguyen(self):
        print("👉 [Bài 7 & 9] Phân tích chữ số, số đối xứng và Armstrong:")
        p = self.head
        while p is not None:
            n = p.data

            t = n
            so_chu_so = 0
            while t > 0:
                so_chu_so += 1
                t //= 10
            if n == 0: so_chu_so = 1

            t = n
            tong_chu_so = 0
            dao_nguoc = 0
            tong_armstrong = 0
            chu_so_cuoi = n % 10

            while t > 0:
                digit = t % 10
                tong_chu_so += digit
                dao_nguoc = dao_nguoc * 10 + digit
                tong_armstrong += digit ** so_chu_so
                t //= 10

            is_doi_xung = (dao_nguoc == n)
            is_armstrong = (tong_armstrong == n)

            print(
                f"   - Số {n}: Số chữ số={so_chu_so}, Tổng={tong_chu_so}, Cuối={chu_so_cuoi}, Đối xứng={is_doi_xung}, Armstrong={is_armstrong}")
            p = p.next

    # --- BÀI 8: ĐỔI THẬP PHÂN SANG NHỊ PHÂN ---
    def doi_sang_nhi_phan(self):
        print("👉 [Bài 8] Chuyển đổi các số sang hệ nhị phân:")
        p = self.head
        while p is not None:
            n = p.data
            if n == 0:
                print(f"   - Số {n} -> Nhị phân: 0")
                p = p.next
                continue

            temp = n
            so_du_list = []
            while temp > 0:
                so_du = temp % 2
                so_du_list.append(str(so_du))
                temp //= 2

            so_du_list.reverse()
            nhi_phan = "".join(so_du_list)
            print(f"   - Số {n} -> Nhị phân: {nhi_phan}")
            p = p.next


# ================= KHỞI TẠO VÀ IN KẾT QUẢ =================
ds = DSLK()
du_lieu = [2, 5, 7, 3, 4, 6, 8, 2, 9, 10, 11]
for x in du_lieu:
    ds.themcuoi(x)

# In danh sách ban đầu trước khi chạy thuật toán
ds.inds()
print("=" * 50)

# Thực thi lần lượt các bài từ 5 đến 10
ds.tim_doan_tang_dai_nhat()
print("-" * 50)
ds.tim_cap_tong_bang_k(10)
print("-" * 50)
ds.phan_tich_so_nguyen()
print("-" * 50)
ds.doi_sang_nhi_phan()