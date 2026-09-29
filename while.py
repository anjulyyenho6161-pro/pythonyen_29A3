i=1
while i<5:
    print("a")
    i=i+1 #  câu lệnh tác động đến  điều kiện để dừng
for y in range(5):
    print(y)
for x in range(5,10):
    print(x)
for a in range(10,15,2):
    print(a)
for b in range(2,8,2):
    if b==5:
        break
        continue
    else:
        print(b)
