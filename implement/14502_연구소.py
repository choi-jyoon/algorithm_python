n, m = map(int, input().split())
graph = []

for i in range(n):
    arr = list(map(int, input().split()))
    graph.append(arr)
    
print(graph)