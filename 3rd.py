n=int(input())
shift=0
allfamilies=[]
families=[]
possible=[]

for i in range(n):
    families.append[i]
    
for i in range(n):
    m=input()
    m=list(map(int,m.split(" ")))
    allfamilies.append(m)
    
for j in allfamilies:
    jcantvisit=families
    jcantvisit=set(jcantvisit)-set(j)
    x=allfamilies.index(j)
    jcantvisit.pop(x)
    possible=jcantvisit
    if possible==[]:
        shift+=1
    else:
        
        families.pop()
    
