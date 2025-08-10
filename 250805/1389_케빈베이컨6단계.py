n, m = map(int, input().split())
graph = [[1e9 for _ in range(n+1)] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1
    
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
            
# print(graph)
answer = []
min_bacon = 1e9
for i in range(1, n+1):
    bacon = 0
    for j in range(1, n+1):
        if i !=j:
            bacon += graph[i][j]
    answer.append((bacon, i))
    if bacon <min_bacon:
        min_bacon = bacon
        ans = i
    
print(ans)