import sys
sys.setrecursionlimit(100000)

n = int(input())
graph = [[0 for _ in range(n)] for _ in range(n)]
rggraph = [[0 for _ in range(n)] for _ in range(n)]
visited = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    arr = input()
    for j in range(n):
        graph[i][j] = arr[j]
        if arr[j] == 'G':
            rggraph[i][j] = 'R'
        else:
            rggraph[i][j] = arr[j]

    
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def dfs(x, y, cur, graph, visited):
    visited[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0<=nx<n and 0<=ny<n:
            if graph[nx][ny] == cur and visited[nx][ny] == 0:
                dfs(nx, ny, cur, graph, visited)
                    
    return True

answer = 0
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            dfs(i, j, graph[i][j], graph, visited)
            answer +=1

rgvisited = [[0 for _ in range(n)] for _ in range(n)]

rganswer = 0
for i in range(n):
    for j in range(n):
        if rgvisited[i][j] == 0:
            dfs(i, j, rggraph[i][j], rggraph, rgvisited)
            rganswer +=1
print(answer, rganswer)