from collections import deque

n, k = map(int, input().split())
visited = [0] * 100001
q = deque()
q.append(n)
visited[n] = 0
cnt = 0
while q:
    x = q.popleft()
    
    if x == k:
        cnt = visited[x]
        break
    
    if x-1>=0 and visited[x-1] == 0:
        q.append(x-1)
        visited[x-1] = visited[x] +1
    if x+1 <=100000 and visited[x+1] == 0:
        q.append(x+1)
        visited[x+1] = visited[x] +1
    if 2*x <=100000 and visited[2*x] == 0:
        q.append(2*x)
        visited[2*x] = visited[x] +1
        
print(cnt)