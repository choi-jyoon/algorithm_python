from collections import deque

n, k = map(int, input().split())
visited = [0] * 100003

### n -> k 로 가는 최단 경로 최단 시간 구하기: bfs (s+1, s-1, 2*s)
q = deque()
q.append((n, 0))

while q:
    x, dist = q.popleft()
    if x == k:
        print(dist)
        break
    
    if 0<=2*x<100002 and visited[2*x] == 0:
        visited[2*x] = 1
        q.append((2*x, dist))
    if 0<=x-1<100002 and visited[x-1] == 0:
        visited[x-1] +=1
        q.append((x-1, dist+1))
    if 0<=x+1<100002 and visited[x+1] == 0:
        visited[x+1] +=1
        q.append((x+1, dist+1))
    
