t=int(input())
l=[]
'''def fibonacci(n):
    if n==0:
        return 1
    elif n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
'''
def fibonacci(n):
    x,y= 1,1
    for i in range(0,n):
        x,y=y,x+y
    return x
        

for i in range(t):
    n=int(input())
    fibval=fibonacci(n)
    l.append(fibval%10)

for i in l:
    print(i)
