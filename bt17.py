n=int(input("nhập vào số n"))
i=1
sum=0
'''while i<=n:
    if n % i == 0:
        sum += i
        if i != n // i:
           sum += n // i
            break
        print("là số hoàn hảo")'''
for i in range(1,n+1,1):
    if n %i==0 :
        sum += i
        '''if i != n // i:
           sum += n // i'''
    if sum==n:
        print ("là so hoan hao")
    else:
        print(" không là số hoàn hảo ")

