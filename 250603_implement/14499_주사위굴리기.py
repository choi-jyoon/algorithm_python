n, m, x, y, k = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
move = list(map(int, input().split()))

# 동서북남 순서대로 방향 표시
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

dice = [0, 0, 0, 0, 0, 0]

def move_dice(dir):
    global dice
    top, bottom, left, right, front, back = dice[0], dice[1], dice[2], dice[3], dice[4], dice[5]
    # 동쪽 이동
    if dir == 1:
        dice[0] = left
        dice[1] = right
        dice[2] = bottom
        dice[3] = top
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
    # 남쪽 이동
    if dir == 4:
        dice[0] = back
        dice[1] = front
        dice[4] = top
        dice[5] = bottom


# k 번 명령대로 이동
for d in move:
    nx = x + dx[(d-1)]
    ny = y + dy[(d-1)]
    # print(d, nx, ny, graph[nx][ny])
    # print(d, nx, ny)
    if 0<=nx<n and 0<=ny<m:
        # print(graph[nx][ny])
        move_dice(d)
        if graph[nx][ny] == 0:
            graph[nx][ny] = dice[1]
        else:
            dice[1] = graph[nx][ny]
            graph[nx][ny] = 0
        print(dice[0])
        x = nx
        y = ny
    
    