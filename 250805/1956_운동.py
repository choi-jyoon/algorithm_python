v, e = map(int, input().split())
graph = [[1e9 for _ in range(v+1)] for _ in range(v+1)]

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a][b] = c
    
### 처음과 끝이 같은 사이클 만들기 (도로 길이의 합이 최소)
### 1~v 번까지의 모든 사이클 탐색 

import heapq

visited = [[100000 for _ in range(v+1)] for _ in range(v+1)]

for k in range(1, v+1):
    for i in range(1, v+1):
        for j in range(1, v+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
        
ans = 1e9 
for i in range(v):
    ans = min(ans, graph[i][i])
    # print(graph[i][i])
    
if ans >=1e9:
    ans = -1
print(ans)