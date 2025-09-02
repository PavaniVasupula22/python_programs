n=int(input())
f=0
if n<2:
    f=1
else:
    for i in range(2,int(pow(n,0.5))+1):
        if n%i==0:
            f=1
            break
if(f==0):
    print("Prime")
else:
    print("Not Prime")