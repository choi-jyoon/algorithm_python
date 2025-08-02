n, m = map(int, input().split())
ladders = []
for _ in range(n):
    x, y = map(int, input().split())
    ladders.append([x,y])
    
snakes = []
for _ in range(m):
    u, v = map(int, input().split())
    snakes.append([u,v])
    
graph = [ x for x in range(101)]
visited = [ False for _ in range(101)]

for ladder in ladders:
    graph[ladder[0]] = ladder[1]
    
for snake in snakes:
    graph[snake[0]] = snake[1]

### graph[0] -> graph[99] 로 이동하는 최소 횟수 
### 주사위 굴려서 이동 1~6 까지의 수 중 나오는 수만큼 +x 

from collections import deque 


queue = deque()
queue.append((1, 0))
visited[1] = True
ans = 0

while queue:
    x, ans = queue.popleft()
    if x == 100:
        break
    
    for i in range(1,7):
        nx = x + i
        
        if nx<101 and visited[graph[nx]] == False:
                visited[graph[nx]] = True
                queue.append((graph[nx], ans+1))
                

print(ans)