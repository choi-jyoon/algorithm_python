r, c, t = map(int, input().split())
graph = []
for _ in range(r):
    graph.append(list(map(int, input().split())))
    
    
for i in range(r):
    for j in range(c):
        # 공기청정기 위치 찾기 s, e 로 두 섹션으로 나누기
        if graph[i][j] == -1:
            s = i
            e = i+1
            break
    break
up_graph = [[0 for _ in range(c)] for _ in range(s+1)]
down_graph = [[0 for _ in range(c)] for _ in range(e, r)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

for _ in range(t):
    # 먼지 확산 단계
    for x in range(r):
        for y in range(c):
            if graph[x][y] != 0:
                # 미세먼지 확산
                meonji = graph[x][y] //5
                direc = 0
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    
                    if 0<=nx<r and 0<=ny<c and graph[nx][ny] != -1:
                        graph[nx][ny] += meonji
                        direc +=1
                graph[x][y] -= (meonji * direc)
                
    # 공기청정기 단계
    prev = 0
    for i in range(s, -1, -1):
        for j in range(c):
            prev = graph[i][j]
            
            