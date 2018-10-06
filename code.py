class Node:                                  #creating a node for a single line
    def __init__(self,listofcord):
        self.listofcord=listofcord
        self.x1=listofcord[0]
        self.y1=listofcord[1]
        self.x2=listofcord[2]
        self.y2=listofcord[3]
        self.left=None
        self.right=None
        self.front=[]
        self.back=[]


class bspTree:
    def __init__(self,S):
        self.root=Node(lines[S])             #root is the address of the root node
        lines.pop(S)                 
        self.insert_node(self.root)
        for i in lines:
            j=Node(i)
            self.insert_node(j)
        for i in newlines:
            j=Node(i)
            self.insert_node(j)
        self.frontmost(self.root)
        print("front of all:-",frnt.pop())
        #self.traverse(self.root)            #if want to traverse the whole tree
        #self.frontandback(self.root)        #if want to print front lines and back lines of the root line

        
    def check_d(self,node,line):
        d1=(node.x1-line.x1)*(line.y2-line.y1)-(node.y1-line.y1)*(line.x2-line.x1)
        d2=(node.x2-line.x1)*(line.y2-line.y1)-(node.y2-line.y1)*(line.x2-line.x1)
        return d1,d2


    def intersect_point(self,node,line):
        if (line.x2-line.x1)!=0 and (node.x2-node.x1)!=0:
            m1=(line.y2-line.y1)/(line.x2-line.x1)
            m2=(node.y2-node.y1)/(node.x2-node.x1)
            y= ((m1*m2)*(node.x1-line.x1)+(line.y1*m2)-(node.y1*m1))/(m2-m1)
            x=((line.x1*m1)-(node.x1*m2)+(node.y1-line.y1))/ (m1-m2)
            return x,y
        
        elif (line.x2-line.x1)==0:
            m2=(node.y2-node.y1)/(node.x2-node.x1)
            y=m2*(line.x1-node.x2)+ node.y2
            return line.x1,y
        
        elif (node.x2-node.x1)==0:
            m1=(line.y2-line.y1)/(line.x2-line.x1)
            y=m1*(node.x1-line.x2)+line.y2
            return node.x1,y


    def insert_node(self,node):
        current=self.root                                  #node,current,root are object addresses
        
        if node!=self.root:
            while True:
                d1,d2=self.check_d(node,current)
                
                if (d1>0 and d2>0) or (d1>0 and d2==0) or (d2>0 and d1==0):
                    current.front.append(node.listofcord)
                    if current.right==None:
                        current.right=node
                        break
                    else:
                        current=current.right
                        
                elif (d1<0 and d2<0) or (d1<0 and d2==0) or (d2<0 and d1==0):
                   current.back.append(node.listofcord)
                   if current.left==None:
                       current.left=node
                       break
                   else:
                       current=current.left
                       
                elif (d1>0 and d2<0)or (d1<0 and d2>0): 
                   x,y=self.intersect_point(node,current)
                   newlines.append([node.x1,node.y1,x,y])
                   newlines.append([node.x2,node.y2,x,y])
                   break
                
                elif d1==0 and d2==0:
                    break
        

    def traverse(self,node):
        if node is not None:
            print(node.listofcord)                        #traversing the whole tree using preorder
            print(node.front)
            print(node.back)     
            self.traverse(node.right)
            self.traverse(node.left)

    def frontmost(self,node):                             #using inorder traversal
        if node is not None:
            self.frontmost(node.left)
            frnt.append(node.listofcord)
            print(node.listofcord)
            self.frontmost(node.right)

    def frontandback(self,node):                          #front lines list and back lines list of the given line(starting line) 
        print("Front lines:- ",node.front)
        print("Behind lines:- ",node.back)

N=int(input())              #no of lines
S=int(input())              #starting line number of the code
S=S-3                       #index of the starting line

lines=[]                    #all the cordinates of lines
oneline=[]                  #cordinates of a line
newlines=[]                 #newly created lines after intersecting 2 lines
frnt=[]                     #stores the lines from back to front

for i in range(N):
    a=input() 
    
    for j in a.split(","):      #split method return a list
        b=j.strip("(")
        b=b.strip(")")
        oneline.append(b)       
    lines.append(oneline)       #[[],[],[],...]
    oneline=[]

for i in range(N):
    lines[i]=list(map(int,lines[i]))    #converting cordinates to integers



a=bspTree(S)

'''
test data set:-

7
6
(2,6),(6,6)
(-5,3),(-5,6)
(2,2),(4,5)
(-2,2),(-4,4)
(-5,1),(-3,3)
(-4,4),(-2,6)
(2,8),(4,7)

'''
