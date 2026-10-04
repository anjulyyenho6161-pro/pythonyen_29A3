#viết chương trình tạo một danh sách các số nguyên sau đó thực hiện các thao tác sau:

n=int(input("nhâp vào số pt n: "))
ds=[]
tongchan=0
tongle=0
# Dùng vòng lặp for để nhập từng phần tử a[i]
for i in range(n):
    # Nhập giá trị cho phần tử thứ i
    gia_tri = float(input(f"Nhập phần tử a[{i}]: "))
    # Thêm giá trị vào danh sách
    ds.append(gia_tri)

# In danh sách sau khi nhập
print("Danh sách vừa nhập là:", ds)
# a> in ra màn hình số phần tử của danh sách
sopt=len(ds)
print("số phần tử có trong danh sách là:", sopt)
#b>tìm pt lớn nhất , nhỏ nhất và tinh trung  bìnhcacs giá trị của danh sách
print("phần tử lớn nhất trong ds là:",max(ds))
print("phần tử nhỏ nhất trong danh sách là:", min(ds))
print("trung bình các giá trị của ds là:",sum(ds)//sopt)
#c>tính tổng các số chẵn lẻ có trong ds
for i in range(1,sopt+1):
    if i%2==0:
        tongchan+=i
    else:
        tongle+=i
print("tổng chẵn là:", tongchan)
print("tổng lẻ là:", tongle)

