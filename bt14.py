n=int(input("nhap vào số n: "))
s=0
i=1
'''while i<=n:
    s=s+i
    i=i+1'''
for i in range(1,n+1):
    s=s+i
    i+=1
print(f"tổng số từ 1 dến n: {s}")