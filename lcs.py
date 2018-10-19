
x="abcdcdab"
y="dcbcaa"

m=len(x)
n=len(y)

c=[[0 for _ in range(m+1)] for __ in range(n+1)]
b=[["" for _ in range(m+1)] for __ in range(n+1)]

for i in range(1,m):
    for j in range(1,n):
        if (x[i]==y[j]):
            c[i][j]=c[i-1][j-1]+1
            b[i][j]="/^"
        elif(c[i-1][j] >= c[i][j-1]):
            c[i][j]=c[i-1][j]
            b[i][j]="|^"
        else:
            c[i][j]=c[i][j-1]
            b[i][j]="<_"

print(c)
print(b)