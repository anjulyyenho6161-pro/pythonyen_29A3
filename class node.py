class Node:#một nút
    def __init__(self,data):
        self.data=data#truyền dữ liệu vào dta cuối
        self.next=None#con trỏ tới vị trí kế tiếp
class DSLK:#một danh sách
    def __init__(self):
        self.head=None
    def themdau(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node
    def inds(self):
        p=self.head
        while p is not None:
            print(p.data,end="-")
            p=p.next
        print("None")
    def themcuoi(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            return
        p=self.head
        while p.next is not None:#last.next
            p=p.next
        p.next=new_node
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
    def timkiem(self,x):
        if self.head is None:
            return None
        p=self.head
        while p:#p is not None
            if p.data ==x:
                return p
            p=p.next
        return None

    def sapxep(self):
        if self.head is None:
            return None

        p = self.head
        while p:
            q = p.next
            while q:
                if p.data > q.data:
                    p.data, q.data = q.data, p.data
                q = q.next
            p = p.next





ds=DSLK()
ds.themdau(3)
ds.themdau(9)
ds.themdau(5)
ds.themdau(1)
ds.inds()
ds1=DSLK()
ds1.themdau(8)
ds1.themdau(6)
ds1.inds()
ds2=DSLK()
n=10
for i in range(1,n+1):#range(n)  ds2.themdau(i+1)
    ds2.themdau(i)
ds2.inds()
n=20
for i in range(1,n+1):
    if i%3==0:
        ds2.themcuoi(i)
ds2.inds()
ds2.chiahetcho2()
x=int(input("nhập vào giá trị x: "))
kq=ds2.timkiem(x)
if kq is not None:
    print(f"tìm thấy {x} trong ds2")
else:
    print(f"không tim thấy {x} trong ds2 ")
print('ds2 trước khi sắp xếp')
ds2.inds()
ds2.sapxep()
print("ds2 sau khi sắp xếp")
ds2.inds()











