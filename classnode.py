class Node:  # Một nút
    def __init__(self, data):
        self.data = data  # Truyền dữ liệu vào data
        self.next = None  # Con trỏ tới vị trí kế tiếp


class DSLK:  # Một danh sách
    def __init__(self):
        self.head = None

    # 1. Thêm vào đầu danh sách
    def themdau(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # 2. Thêm vào cuối danh sách
    def themcuoi(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        p = self.head
        while p.next is not None:
            p = p.next
        p.next = new_node

    # 3. Xóa một phần tử theo giá trị
    def xoa(self, key):
        p = self.head
        if p is not None and p.data == key:
            self.head = p.next
            print(f"Đã xóa '{key}' khỏi danh sách.")
            return

        prev = None
        while p is not None and p.data != key:
            prev = p
            p = p.next

        if p is None:
            print(f"Không tìm thấy '{key}' trong danh sách để xóa.")
            return

        prev.next = p.next
        print(f"Đã xóa '{key}' khỏi danh sách.")

    # 4. Tìm kiếm một phần tử
    def timkiem(self, key):
        p = self.head
        vi_tri = 1
        while p is not None:
            if p.data == key:
                return vi_tri
            p = p.next
            vi_tri += 1
        return -1  # Không tìm thấy

    # 5. Sắp xếp danh sách (Tăng dần)
    def sapxep(self):
        if self.head is None:
            return

        vi_doi = True
        while vi_doi:
            vi_doi = False
            p = self.head
            while p.next is not None:
                if p.data > p.next.data:
                    p.data, p.next.data = p.next.data, p.data
                    vi_doi = True
                p = p.next

    # 6. Tính độ dài danh sách liên kết
    def tinh_do_dai(self):
        dem = 0
        p = self.head
        while p is not None:
            dem += 1
            p = p.next
        return dem

    # 7. Tìm số lớn nhất, nhỏ nhất và các vị trí tương ứng
    def tim_max_min(self):
        if self.head is None:
            print("Danh sách đang trống!")
            return

        max_val = self.head.data
        min_val = self.head.data

        max_pos = []
        min_pos = []

        p = self.head
        vt = 1
        while p is not None:
            if p.data > max_val:
                max_val = p.data
                max_pos = [vt]
            elif p.data == max_val:
                max_pos.append(vt)

            if p.data < min_val:
                min_val = p.data
                min_pos = [vt]
            elif p.data == min_val:
                min_pos.append(vt)

            p = p.next
            vt += 1

        print(f"👉 Giá trị lớn nhất là: {max_val}, nằm ở vị trí thứ: {max_pos}")
        print(f"👉 Giá trị nhỏ nhất là: {min_val}, nằm ở vị trí thứ: {min_pos}")

    # 8. Hàm in danh sách (kết hợp in luôn độ dài)
    def inds(self):
        p = self.head
        print("Danh sách: ", end="")
        while p is not None:
            print(p.data, end=" -> ")
            p = p.next
        print("None")
        print(f"👉 Độ dài danh sách (số lượng phần tử): {self.tinh_do_dai()}")
    def chiahetcho2(self):
        if self.head is None:
            return
        print('danh sách các số chia hết cho 2: ')
        p=self.head
        tong=0
        while p:
            if p.data % 2==0:
                print(p.data, end="-")
                tong+=p.data
            p= p.next
        print("tong",tong)


# ================= THỬ NGHIỆM CHƯƠNG TRÌNH =================
if __name__ == "__main__":
    ds = DSLK()

    # 1. Thêm đầu & thêm cuối
    ds.themdau(10)  # Danh sách: 10
    ds.themdau(5)  # Danh sách: 5 -> 10
    ds.themcuoi(20)  # Danh sách: 5 -> 10 -> 20
    ds.themcuoi(15)  # Danh sách: 5 -> 10 -> 20 -> 15

    print("👉 Danh sách ban đầu:")
    ds.inds()

    # 2. Tìm kiếm
    gia_tri_tim = 20
    vt = ds.timkiem(gia_tri_tim)
    if vt != -1:
        print(f"🔍 Tìm thấy {gia_tri_tim} tại vị trí thứ {vt}")
    else:
        print(f"🔍 Không tìm thấy {gia_tri_tim}")

    # 3. Sắp xếp
    print("\n👉 Sau khi sắp xếp tăng dần:")
    ds.sapxep()
    ds.inds()

    # 4. Xóa
    print()
    ds.xoa(10)
    print("👉 Sau khi xóa số 10:")
    ds.inds()

    # 5. Thêm thêm dữ liệu để test Max, Min và vị trí
    ds.themcuoi(12)
    ds.themcuoi(5)
    ds.themcuoi(25)
    ds.themcuoi(5)  # Trùng giá trị nhỏ nhất
    ds.themcuoi(25)  # Trùng giá trị lớn nhất

    print("\n" + "=" * 15 + " KẾT QUẢ SAU KHI THÊM THÊM PHẦN TỬ " + "=" * 15)
    ds.inds()

    print("-" * 45)

    # 6. Tìm max, min và vị trí
    ds.tim_max_min()
