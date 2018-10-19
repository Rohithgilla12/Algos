import sys
n=4
x=[sys.maxsize for _ in range(n)]
def Place(k,i):
    """
    To check if we can place the queen there or not
    """
    for j in range(k):
        if((x[j]==i) or (abs(i-x[j])==abs(j-k))):
            return False
    return True

def NQueens(k,n):
    """
    Driver Function
    """
    for i in range(n):
        if Place(k,i):
            x[k]=i
            if k is n-1:
                print(x)
            else:
                NQueens(k+1,n)

NQueens(0,n)