import heapq 

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    
start, dest = map(int, input().split())
visited = [1e9 for _ in range(n+1)]
visited[start] = 0
pq = [(0, start)]

while pq:
    cost, pos = heapq.heappop(pq)
    if cost > visited[pos]:
        continue
    if pos == dest:
        break
    for y, c in graph[pos]:
        nxt = cost + c
        if visited[y] > nxt:
            visited[y] = nxt
            heapq.heappush(pq, (nxt, y))
            
print(visited[dest])