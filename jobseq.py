
arr = [['a', 2, 100],
       ['b', 1, 19], 
       ['c', 2, 27], 
       ['d', 1, 25], 
       ['e', 3, 15]]

n = len(arr)
free=3

arr = sorted(arr,key=lambda x : -1*x[-1])
result = [False]*free
jobs=[-1]*free

for i in range(len(arr)):
    for j in range(min(free-1, arr[i][1] - 1), -1, -1):
        if result[j] is False:
            result[j]=True
            jobs[j]=arr[i][0]
            break

print(jobs)