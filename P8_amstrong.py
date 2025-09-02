n=int(input())
s=0
t=n
l=len(str(n))
while n!=0:
    d=n%10
    s=s+pow(d,l)
    n=n//10
if(s==t):
    print("amstrong")
else:
    print("not amstrong")