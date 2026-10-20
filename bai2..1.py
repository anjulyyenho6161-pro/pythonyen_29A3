n= int(input("nhap so pt của dãy: "))
A=[]
for i in range(n):
    print(f"phần tử thứ A[{i}]=",end='')
    A.append(float(input()))
print(A)
dat=0
khongdat=0
maxd=A[0]
B=[]
vtmax=0
for i in range(len(A)):
     if A[i]>=5:
         dat=dat+1
     else:
         khongdat=khongdat+1
     if A[i]>7:
         B.append(A[i])
     if A[i]>maxd:
         maxd=A[i]
         vtmax=i

print(f"Số lượng phần tử đạt (>=5): {dat}")
print(f"Số lượng phần tử không đạt (<5): {khongdat}")
print(f"Các phần tử lớn hơn 7 (B): {B}")
print(f"Phần tử lớn nhất là {maxd} tại vị trí A[{vtmax}]")