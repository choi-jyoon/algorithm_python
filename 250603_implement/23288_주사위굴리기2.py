n, m, k = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))


# 동남서북 순서대로 방향 표시
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

dice = [1,6,4,3,5,2]

def move_dice(dir):
    global dice
    top, bottom, left, right, front, back = dice[0], dice[1], dice[2], dice[3], dice[4], dice[5]
    # 동쪽 이동
    if dir == 0:
        dice[0] = left
        dice[1] = right
        dice[2] = bottom
        dice[3] = top
    # 남쪽 이동
    if dir == 1:
        dice[0] = back
        dice[1] = front
        dice[4] = top
        dice[5] = bottom
    # 서쪽 이동
    if dir == 2:
        dice[0] = right
        dice[1] = left
        dice[2] = top
        dice[3] = bottom
    # 북쪽 이동
    if dir == 3:
        dice[0] = front
        dice[1] = back
        dice[4] = bottom
        dice[5] = top

score = 0
x,y = 0, 0
d = 0

visited = [[0 for _ in range(m)] for _ in range(n)]
cnt = 0
def dfs(x, y, num):
    global cnt
    visited[x][y] = 1
    cnt +=1
    # print(cnt)
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # print(nx, ny, graph[nx][ny], visited[nx][ny])
        if 0<=nx<n and 0<=ny<m and visited[nx][ny] == 0 and graph[nx][ny] == num:
            dfs(nx, ny, num)
    
# k 번 명령대로 이동
for i in range(k):
    nx = x + dx[(d)]
    ny = y + dy[(d)]
    # print(d, nx, ny, graph[nx][ny])
    # print(d, nx, ny)
    
    if nx<0 or nx>=n or ny<0 or ny>=m:
    # 이동 불가능한 경우 : 이동 방향 반대로 한칸
        # print(nx, ny, d)
        d = (d+2) % 4
        # print(d)
        nx = x + dx[(d)]
        ny = y + dy[(d)]

    # print(graph[nx][ny])
    move_dice(d)
    visited = [[0 for _ in range(m)] for _ in range(n)]
    cnt = 0
    dfs(nx, ny, graph[nx][ny])
    # print(nx, ny, d, cnt, graph[nx][ny])
    # print(dice[1], graph[nx][ny])
    score += (cnt * graph[nx][ny])
    
    if dice[1] >  graph[nx][ny]:
        # 시계방향 90도 회전
        d = (d+1) % 4
    elif dice[1] < graph[nx][ny]:
        # 반시계 방향 90도 회전
        d = (d+3) % 4
    else:
        d = d
    x = nx
    y = ny

        
        
print(score)