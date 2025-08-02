n, k = map(int, input().split())
visited = [False] * 100001
from collections import deque 

q = deque()
q.append((n, 0))
visited[n] = True
ans = 0
while q:
    x, c = q.popleft()
    
    if x == k:
        ans = c
        break
    
    if x + 1<=100000 and visited[x+1]==False:
        visited[x+1] = True
        q.append((x+1, c+1))
    if x-1>=0 and visited[x-1] == False:
        visited[x-1] = True
        q.append((x-1, c+1))
    if 2*x <= 100000 and visited[2*x] == False:
        visited[2*x] = True
        q.append((2*x, c+1))
        
print(ans)
    