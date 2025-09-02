'''
a=0
b=1
n=int(input("enter a num"))
for i in range(n):
    c=a+b
    print(a,end=" ")
    a=b
    b=c
'''
#recursion
def fib(n):
    if n<=1:
        return n
    else:
        return fib(n-1) + fib(n-2)
for i in range(10):
    print(fib(i), end=" ")
