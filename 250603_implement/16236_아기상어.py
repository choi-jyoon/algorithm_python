from collections import deque

n = int(input())
graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))
    
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]
visited = [[False for _ in range(n)] for _ in range(n)]

def bfs(x, y, d, shark):
    global ate
    q = deque()
    q.append((x,y, d))
    
    while q:
        x,y, d = q.popleft()
        
        for i in range(4):
            nx= x+dx[i]
            ny = y + dy[i]
            
            if 0<=nx <n and 0<=ny<n:
                if graph[nx][ny] != 0 and graph[nx][ny]< shark:
                    graph[nx][ny] = 0
                    ate +=1
                    q.append((nx, ny, d+1))
        
    return 
                    
                    
def find_fish(shark):
    fish = 0
    for i in range(n):
        for j in range(n):
            if 0<graph[i][j] <shark:
                fish +=1
                
    return fish 

shark = 2
finish = True
ans = 0
ate = 0
while finish:
    fish = find_fish(shark)
    if fish == 0:
        finish = False
        break
    for _ in range(fish):
        for i in range(n):
            for j in range(n):
                if ate == shark:
                    shark +=1
                if graph[i][j] == 9:
                    bfs(i, j, ans, shark)
        
    
print(ans)
        
                