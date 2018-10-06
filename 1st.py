import itertools

topics=[]
time=[]

while True:
    n=input()
    if n=="":
        break
    l=n.split(" ")
    time.append(int(l[0]))
    del l[0]
    for i in l:
        if i not in topics:
            topics.append(i)
        
print(time)
print (topics) 

stuff = [[1, 2, 3],[4,5],[7,8,9]]
for L in range(1, len(stuff)+1):
    for subset in itertools.combinations(stuff, L):
        subset=list(subset)
        print(subset)
        if set(subset)==set(topics):
            print("kkkkkkk")
        print(subset)

