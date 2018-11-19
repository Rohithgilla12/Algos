from texttable import Texttable
x="abcdcdab"
y="dcbcaa"

m=len(x)
n=len(y)

# L=[[0 for _ in range(m+1)] for __ in range(n+1)]
# for i in range(m+1):
#     for j in range(n+1):
#         if i==0 or j==0:
#             L[i][j]=0
#         elif x[i-1] == y[j-1]:
#             L[i][j]=L[i-1][j-1]+1
#         else:
#             L[i][j] = max(L[i-1][j],L[i][j-1])    

#     index = L[m][n]           
#     lcs=["" for _ in range(index+1)] 
#     lcs[index]=""
#     i=m
#     j=n
#     while i>0 and j>0:
#         if x[i-1] == y[j-1]:
#             lcs[index-1]=x[i-1]
#             i=i-1
#             j=j-1
#             index-=1
#         elif L[i-1][j] > L[i][j-1]: 
#             i-=1
#         else: 
#             j-=1
  
#     print ("LCS of " + x + " and " + y + " is " + "".join(lcs))
  

# c=[[0 for _ in range(m+1)] for __ in range(n+1)]
# b=[["" for _ in range(m+1)] for __ in range(n+1)]

# for i in range(1,m):
#     for j in range(1,n):
#         if (x[i-1]==y[j-1]):
#             c[i][j]=c[i-1][j-1]+1
#             b[i][j]="\^"
#         elif(c[i-1][j] >= c[i][j-1]):
#             c[i][j]=c[i-1][j]
#             b[i][j]="|^"
#         else:
#             c[i][j]=c[i][j-1]
#             b[i][j]="<_"

# print(c)
# print(b)



def lcs(X, Y, m, n): 
    L = [[0 for x in range(n+1)] for x in range(m+1)] 
    for i in range(m+1): 
        for j in range(n+1): 
            if i == 0 or j == 0: 
                L[i][j] = 0
            elif X[i-1] == Y[j-1]: 
                L[i][j] = L[i-1][j-1] + 1
            else: 
                L[i][j] = max(L[i-1][j], L[i][j-1])
    x = Texttable()                             
    x.add_rows(L)
    print(x.draw())
    index = L[m][n] 
    lcs = [""] * (index+1) 
    lcs[index] = "" 
    i = m 
    j = n 
    while i > 0 and j > 0: 
        if X[i-1] == Y[j-1]: 
            lcs[index-1] = X[i-1] 
            i-=1
            j-=1
            index-=1
        elif L[i-1][j] > L[i][j-1]: 
            i-=1
        else: 
            j-=1
  
    print ("LCS of " + X + " and " + Y + " is " + "".join(lcs))


m = len(x) 
n = len(y) 
lcs(x, y, m, n)