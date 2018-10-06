n=input()
m=list(map(int,n.split(" ")))
noofvertices=m[0]
class Vertex:
    def __init__(self,key):
        self.id=key            #contains the connected nodes to a one vert
        self.color="white"
        self.connectedTo={}
        self.visited= False
    
    def adjecentNodes(self,nd,weight):
        self.connectedTo[nd]=weight
        
    def getConnections(self):
        return self.connectedTo.keys()   #keys are the objects of vertices
    def getId(self):
        return self.id
    
class Graph:
    def __init__(self):
        self.vertlist={}           #contains all node names as keys and object addresses as values
        self.numVertices=0

    def addVertex(self,key):
        self.numVertices += 1
        newVertex=Vertex(key)
        self.vertlist[key]=newVertex
        return newVertex
    
    def addEdge(self,f,t,weight):
        if f not in self.vertlist:
            newVertex=self.addVertex(f)
        if t not in self.vertlist:
            newVertex=self.addVertex(t)
        self.vertlist[f].adjecentNodes(self.vertlist[t],weight)
    def getObjects(self):
        return self.vertlist.values()



g=Graph()
for i in range(m[0]):
    g.addVertex(i+1)
for j in range(m[1]):
    n1=input()
    m1=list(map(int,n1.split(" ")))
    g.addEdge(m1[0],m1[1],0)
print(g.vertlist)
for v in g.getObjects():
    for w in v.getConnections():
        print("( %s , %s )" % (v.getId(), w.getId()))

