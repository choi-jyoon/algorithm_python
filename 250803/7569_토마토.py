from collections import deque

m, n, h = map(int, input().split())
graph = []
for _ in range(h):
    sub_graph = []
    for _ in range(n):
        arr = list(map(int, input().split()))
        sub_graph.append(arr)
    graph.append(sub_graph)
    
    
# print(graph)

dx = [-1, 0, 0, 1, 0, 0]
dy = [0, -1, 0, 0, 1, 0]
dz = [0, 0, -1, 0, 0, 1]

q = deque()

for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == 1:
                q.append((i, j, k))
                
while q:
    x, y, z = q.popleft()
    
    for i in range(6):
        nx = x + dx[i]
        ny = y + dy[i]
        nz = z + dz[i]
        
        if 0<=nx<h and 0<=ny<n and 0<=nz<m and graph[nx][ny][nz] == 0:
            graph[nx][ny][nz] = graph[x][y][z] +1
            q.append((nx, ny, nz))
answer = 0
for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == 0:
                print(-1)
                exit(0)
            answer = max(answer, graph[i][j][k])
            
print(answer-1)