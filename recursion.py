
#iterative method
'''def fact(n):
    fac=1
    for i in range(n):
        fac=fac*(i+1)
    return fac
a=fact(4)
print(a)


#using recursive function
def fact(n):
    if n==1:
        return 1
    else:
        return n * fact(n-1)

print(fact(5))

def fib(n):
    a=0
    b=1
    for i in range(2,n):
        c=a+b
        a=b
        b=c
        print(c,end=' ')
fib(8)'''

def fib(n):
    if n==1:
        return 1
    elif n==2:
        return 2
    elif n>2:
        return fib(n-1) + fib(n-2)

for i in range(1,10):
    print(fib(i),end=" ")
    