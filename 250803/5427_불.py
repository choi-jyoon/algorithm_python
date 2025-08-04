from collections import deque
import sys 

input = sys.stdin.readline

tc = int(input())
for _ in range(tc):
    w, h = map(int, input().split())
    graph = [[0 for _ in range(w)] for _ in range(h)]
    for i in range(h):
        arr = input()
        for j in range(w):
            graph[i][j] = arr[j]
            if arr[j] == '@':
                s, e = i, j
    # print(graph)
            
    
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    
    fire = [[-1 for _ in range(w)] for _ in range(h)]
    visited = [[0 for _ in range(w)] for _ in range(h)]
    
    # ### 불 번지는 bfs
    q = deque()
    for i in range(h):
        for j in range(w):
            if graph[i][j] == '*':
                q.append((i, j))
                fire[i][j] = 0
                
                
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0<=nx<h and 0<=ny<w and graph[nx][ny] != '#' and fire[nx][ny] == -1:
                fire[nx][ny] = fire[x][y] + 1
                q.append((nx, ny))
        
    q = deque()
    q.append((s, e, 0))
    visited[s][e] =1
    ans = -1
    
    while q:
        x, y, cur = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx<0 or nx>=h or ny<0 or ny>=w:
                ans = cur
                q.clear()
                break
            
            if 0<=nx<h and 0<=ny<w and graph[nx][ny] == '.' and (fire[nx][ny] == -1 or fire[nx][ny]>cur+1) and visited[nx][ny] == 0:
                visited[nx][ny] = visited[x][y] +1
                q.append((nx, ny, cur+1))
        
    
    if ans == -1:
        print("IMPOSSIBLE")
    else:   
        print(ans+1)