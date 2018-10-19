
class Graph:
    def __init__(self,vertices):
        self.V=vertices
        self.graph=[[0 for _ in range(vertices)] for __ in range(vertices)]
    def isSafe(self,v,pos,path):
        if self.graph[path[pos-1]][v] == 0:
            return False
        if v in path:
            return False
        return True
    def HamilRecur(self,path,pos):
        if pos == self.V:
            if self.graph[path[pos-1]][path[0]] == 1:
                return True
            else:
                return False
        for v in range(1,self.V):
            if self.isSafe(v,pos,path):
                path[pos]=v
                if self.HamilRecur(path,pos+1):
                    return True
                path[pos]=-1
        return False
    def HamilCycle(self):
        path=[-1 for _ in range(self.V)]
        path[0]=0
        if not self.HamilRecur(path,1):
            return False
        print(path)
        return True

def main():
    g=Graph(5)
    g.graph=[[0,1,1,0,1],[1,0,1,1,1],[1,1,0,1,0],[0,1,1,0,1],[1,1,0,1,0]]
    g.HamilCycle()

if __name__ == '__main__':
    main()