n=input()
divisors=[]
output=[]
total=0
m=list(map(int,n.split(" ")))
t=m[0]
a=m[1]
b=m[2]

for i in range(t):
    d=int(input())
    while a<(b+1):
        for j in range(1,a+1):
            if a%j==0:
                if j%d!=0:
                    divisors.append(j)
        total+=len(divisors)
        divisors=[]
        a=a+1
    output.append(total)
    a=m[1]
    total=0
for i in output:
    print(i)
    
