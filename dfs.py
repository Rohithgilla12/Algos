from collections import defaultdict
# visited=[False for _ in range(4)]
class Graph:
    def __init__(self):
        self.graph=defaultdict(list)
    def addEdge(self,u,v):
        self.graph[u].append(v)

        
    """    
    def DFS(self,s):
        visited[s]=True
        for i in self.graph[s]:
            if not visited[i]:
                self.DFS(i)
                print(i)
    """

    def DFSRec(self,curr,visited):
        visited[curr]=True
        print (curr)
        for i in self.graph[curr]:
            if not visited[i]:
                self.DFSRec(i,visited)
    
    def DFS(self,s):
        visited=[False for _ in range(len(self.graph))]
        self.DFSRec(s,visited)


if __name__ == '__main__':
    g=Graph()
    g.addEdge(0, 1) 
    g.addEdge(0, 2) 
    g.addEdge(1, 2) 
    g.addEdge(2, 0) 
    g.addEdge(2, 3) 
    g.addEdge(3, 3) 
    g.DFS(0)
