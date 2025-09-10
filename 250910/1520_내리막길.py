m, n = map(int, input().split())

graph = []
for _ in range(m):
    graph.append(list(map(int, input().split())))
    
visited = [[0 for _ in range(n)] for _ in range(m)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

visited[0][0] = 1
visited[m-1][n-1] = 1

for x in range(m-1, -1, -1):
    for y in range(n-1, -1, -1):
        h = graph[x][y]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx <m and 0<=ny<n:
                if graph[nx][ny] > h:
                    visited[nx][ny] += visited[x][y]
                    
print(visited[0][0])

# for x in range(m):
#     for y in range(n):
#         h = graph[x][y]
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if 0<=nx<m and 0<=ny<n:
#                 if graph[nx][ny] < h and visited[x][y] != 0:
#                     print(h, graph[nx][ny])
#                     visited[nx][ny] += visited[x][y]
                    
# print(visited[m-1][n-1])
# print(visited)
