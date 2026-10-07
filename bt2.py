n=int(input("nhập vào số phần tử của dãy: "))
ds=[]
for i in range(n):
    print(f"phần tử thứ A[{i}]",end='')
    ds.append(float(input()))
print(ds)
duong=[]
am=[]
so=[]
tongduong=0
tongam=0
for x in ds:
    if x<0:
        am.append(x)
        tongam=tongam+(abs(x))
    elif x>0:
        duong.append(x)
        tongduong=tongduong+x
    else :
        so.append(x)

print(f"các số 0: {so}|số lượng:{len(so)}")
print(f"Các số âm: {am} | Số lượng: {len(am)} | Tổng các số âm: {tongam}")
print(f"Các số dương: {duong} | Số lượng: {len(duong)} | Tổng các số dương: {tongduong}")





