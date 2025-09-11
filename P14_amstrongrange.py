lower=int(input())
upper=int(input())
for n in range(lower,upper+1):
    l=len(str(n))
    temp=n
    s=0
    while temp>0:
        d=temp%10
        s=s+pow(d,l)
        temp=temp//10
    if(n==s):
        print(n,end=",")