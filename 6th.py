t=int(input())
result=[]
def fibonacci(n):
    x,y= 1,1
    for i in range(0,n):
        x,y=y,x+y
    return x

for i in range(t):
    n=int(input())
    result.append(fibonacci(n))
for i in result:
    print(i)
