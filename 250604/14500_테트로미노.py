n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))
    
# 5개의 테트로미노 한개씩 놓아보기 
tetlomino = []

def find(x,y,dx, dy):
    s = 0
    for i in range(4):
        nx = x+dx[i]
        ny = y + dy[i]
        
        if 0<=nx < n and 0<=ny<m:
            s += graph[nx][ny]
        else:
            return False
    return s

# 첫번째 테트로미노: 일자
dx = [[0, 0, 0, 0], [0,1,2,3], [0,0,1,1], [0,1,2,2], [0,1,2,2], [0,1,2,0],[0,1,2,0], [0,0,0,1], [0,0,0,1], [1,1,1,0], [1,1,1,0], [0,1,1,2], [0,0,1,1], [0,0,1,1], [1,2,0,1], [0,0,0,1], [0,1,2,1], [0,1,2,1], [1,1,1,0]]
dy = [[0, 1, 2, 3], [0,0,0,0], [0,1,0,1], [0,0,0,1], [1,1,1,0], [0,0,0,1], [1,1,1,0], [0,1,2,0], [0,1,2,2], [0,1,2,0], [0,1,2,2], [0,0,1,1], [0,1,1,2], [1,2,0,1], [0,0,1,1], [0,1,2,1], [0,0,0,1], [1,1,1,0], [0,1,2,1]]

ans = 0
for k in range(19):
    for i in range(n):
        for j in range(m):
            s = find(i, j, dx[k], dy[k])
            if s:
                tetlomino.append(s)
                ans = max(ans, s)
            
print(ans)