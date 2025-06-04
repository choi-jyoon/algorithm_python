from collections import deque
import sys
sys.setrecursionlimit(100000)

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int,input().split())))
    
island = 2

dx = [-1, 1, 0, 0]
dy = [0,0,1,-1]

visited = [[False for _ in range(n)] for _ in range(n)]
find = False
def dfs(x,y, c):
    global find
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        
        if 0<=nx<n and 0<=ny<n:
            if not visited[nx][ny] and graph[nx][ny] == 1:
                visited[nx][ny] = True
                graph[nx][ny] = c
                find = True
                dfs(nx, ny, c)
                
for i in range(n):
    for j in range(n):
        if not visited[i][j] and graph[i][j] == 1:
            visited[i][j] = True
            graph[i][j] = island
            dfs(i, j, island)
            island +=1


def get_edges(island_num):
    edges = []
    for i in range(n):
        for j in range(n):
            if graph[i][j] == island_num:
                for k in range(4):
                    ni, nj = i + dx[k], j + dy[k]
                    if 0 <= ni < n and 0 <= nj < n and graph[ni][nj] == 0:
                        edges.append((i, j))
                        break
    return edges

def bfs(start):
    visited = [[-1]*n for _ in range(n)]
    q = deque()
    for x, y in get_edges(start):
        q.append((x, y))
        visited[x][y] = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] > 0 and graph[nx][ny] != start:
                    return visited[x][y]
                if graph[nx][ny] == 0 and visited[nx][ny] == -1:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))
    return int(1e9)
ans = int(1e9)
for i in range(2, island):  # ✅ 범위 수정
    if not get_edges(i):    # ✅ 안전 장치
        continue
    ans = min(ans, bfs(i))
print(ans)