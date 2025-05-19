from collections import deque 

n, m, k, x = map(int,input().split())
graph = [[] for _ in range(n+1)]

for i in range(m):
    x, y = map(int, (input().split()))
    graph[x].append(y)
    graph[y].append(x)
    

q = deque()
q.append(x)
dist = [-1] * (n+1)
dist[x] = 0
while q: 
    d = q.popleft()
    for i in graph[d]:
        if dist[i] == -1:
            dist[i] = dist[d] + 1
            q.append(i)
            
check = False 
answer = []
for i in range(1, n+1):
    if dist[i] == k:
        check = True
        print(i)

if check == False:
    print(-1)