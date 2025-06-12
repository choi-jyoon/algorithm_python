from collections import deque
n, m = map(int, input().split())
graph = [[0 for _ in range(m)] for _ in range(n)]

for i in range(n):
    arr = input()
    for j in range(m):
        graph[i][j] = int(arr[j])

dx = [-1, 1, 0, 0]
dy = [0,0,-1,1]

def bfs():
    visited = [[[-1, -1] for _ in range(m)] for _ in range(n)]
    
    q = deque()
    q.append((0,0,0))

    visited[0][0][0] = 1
    
    while q:
        x, y, broken = q.popleft()
        
        if x == n-1 and y == m-1:
            return visited[x][y][broken]
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # print(nx, ny)
            
            if 0<=nx<n and 0<=ny<m:
                if graph[nx][ny] == 0 and visited[nx][ny][broken] == -1:
                    # print(nx, ny)
                    visited[nx][ny][broken] = visited[x][y][broken] +1
                    q.append((nx, ny, broken))
                if graph[nx][ny] == 1 and broken == 0 and visited[nx][ny][1] == -1:
                    visited[nx][ny][1] = visited[x][y][broken]+1
                    q.append((nx, ny,1))
                    
    return -1
                    
ans = bfs()
    
print(ans)