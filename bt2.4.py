import random
ds=[]
ds1=[]
tongds=[]
n=random.randint(1,50)
for i in range(10):
        ds.append(random.randint(1,50))
        ds1.append(random.randint(1,50))
        tongds.append(ds[i]+ds1[i])
print("ds:", ds)
print("ds1:", ds1)
print("tongds:", tongds)