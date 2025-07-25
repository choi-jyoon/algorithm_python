m, n = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
    
def check_tomato():
    for i in range(n):
        for j in range(m):
            if graph[i][j] ==0:
                return False
    return True 

if check_tomato():
    print(0)
    exit(0)
from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


q = deque()

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            q.append((i,j))
while q:
    x,y = q.popleft()
    
    

    for i in range(4):
        nx = x +dx[i]
        ny = y+ dy[i]
        
        if 0<=nx <n and 0<=ny<m:
            if graph[nx][ny] ==0:
                graph[nx][ny] = graph[x][y] + 1
                # print(nx, ny, c, graph)
                # print(c)
                q.append((nx, ny))
                
answer = 0

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            print('-1')
            exit(0)
        answer = max(answer, graph[i][j])

            
print(answer-1)
