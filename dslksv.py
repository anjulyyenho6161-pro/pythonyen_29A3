class Node:
    def __init__(self,masv,hoten,namsinh,diem):
        self.masv=masv
        self.hoten=hoten
        self.namsinh=namsinh
        self.diem=diem
        self.next=None
class Dslksv:
    def __init__(self):
        self.head=None
    def themcuoi(self,masv,hoten,namsinh,diem):
        new_node=Node(masv,hoten,namsinh,diem)
        if self.head is None:
            self.head=new_node
            return
        p=self.head
        while p.next is not None:#last Node
            p=p.next
        p.next=new_node

    def nhapdssv(self):
        n=int(input("nhập vòa số lượng sinh viên cần nhập : "))
        for i in range(n):
            print(f"nhập sinh viên thứ {i+1}:")
            masv=input("mã sv: ")
            hoten=input("họ tên: ")
            namsinh=int(input("năm sinh:"))
            diem=float(input("điểm: "))
            self.themcuoi(masv, hoten, namsinh, diem)
    def indssv(self):
        if self.head is None:
            print("ds không có phần tử")
            return
        print(f"{'masv':<10}{'hoten':<25}{'namsinh':<15}{'diem':<10}")#căn phải <
        p = self.head
        while p is not None:
            print(f"{p.masv:<10}{p.hoten:<25}{p.namsinh:<15}{p.diem:<10}")
            p = p.next
        print("None")

ds=Dslksv()
ds.nhapdssv()
ds.indssv()
