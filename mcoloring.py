
class Graph:
    def __init__(self,vertices):
        self.V=vertices
        self.graph=[[0 for _ in range(vertices)] for __ in range(vertices)]
    
    def currSafe(self,vertex,colors,color):
        for i in range(self.V):
            if colors[i]==color and self.graph[vertex][i] ==1 :
                return False
        return True

    def graphColoringRec(self,m,colors,v):
        if v==self.V:
            return True
        for c in range(1,m+1):
            if self.currSafe(v,colors,c):
                colors[v]=c
                if self.graphColoringRec(m,colors,v+1):
                    return True
                colors[v]=0
    
    def colorgraph(self,m):
        colors=[0 for _ in range(self.V)]
        if not self.graphColoringRec(m, colors, 0):
            return False
        print (colors)

if __name__ == '__main__':
    g=Graph(4) 
    g.graph = [[0,1,1,1], [1,0,1,0], [1,1,0,1], [1,0,1,0]] 
    m=3
    g.colorgraph(m) 

