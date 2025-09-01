#using Recursiom

def fac(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fac(n-1)
print(fac(6))

"""
#using loops

f=1
n=5
for i in range(1,n+1):
    f=f*i
print(f)

"""
