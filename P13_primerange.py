upper=int(input("enter a number : "))
lower=int(input("enter a number : "))
primes=[]
for i in range(lower,upper+1):
    flag=0
    if i<=1:
        continue
    for x in range(2,int(pow(i,0.5))+1):
        if i%x==0:
            flag=1
            break
    if(flag!=1):
        primes.append(i)
print(primes)
    