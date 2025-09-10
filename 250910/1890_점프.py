n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
    
# graph[0][0] -> graph[n-1][n-1]  로 이동할 수 있는 경로의 수

visited = [[0 for _ in range(n)] for _ in range(n)]

visited[0][0] = 1


for i in range(n):
    for j in range(n):
        k = graph[i][j]
        if k == 0 or visited[i][j] == 0:
            continue
        if i + k <n:
            visited[i+k][j] += visited[i][j]
        if j + k < n:
            visited[i][j+k] += visited[i][j]
        
print(visited[n-1][n-1])