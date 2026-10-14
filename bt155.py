
import random
A=[]
B=[]
n=random.randint(1,10)
for i in range(random.randint(1,10)):
    A.append(random.randint(1,10))
print("dsA",A)
for x in A:
    if x not in B:
        B.append(x)
print("Danh sách B:", B)



