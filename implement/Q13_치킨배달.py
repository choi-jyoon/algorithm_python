from collections import deque
from itertools import combinations

def solution():
    n, m = map(int, input().split())
    graph = []
    for i in range(n):
        arr = list(map(int, input().split()))
        graph.append(arr)
    
    chickens = find_chicken(graph, n)
    chicken_combs = list(combinations(chickens, m))
    
    total_dist = 1e9
    
    answer = 0
    for i in range(n):
        for j in range(n):
            if graph[i][j]==1:
                total_dist =min(total_dist,  get_distance([i,j], chicken_combs[0]))
                answer += total_dist
        
    print(total_dist)
                
            
def find_chicken(graph, n):
    chickens = []
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 2:
                chickens.append((i, j))
    return chickens

def get_distance(home, chicken):
    n = len(chicken)
    dist = 1e9

    for i in range(n):
        dist = min(dist, abs(home[0] - chicken[i][0]) + abs(home[1] - chicken[i][1]))
        
    return dist

solution()