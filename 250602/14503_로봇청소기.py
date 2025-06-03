import sys
sys.setrecursionlimit(100000)

n, m = map(int, input().split())
r, c, d = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

# 북, 동, 남, 서 → 반시계: (d+3)%4
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

answer = 0

def cleaning(x, y, d):
    global answer
    if graph[x][y] == 0:
        graph[x][y] = 2
        answer += 1

    for _ in range(4):
        # 반시계 회전
        d = (d + 3) % 4
        nx = x + dx[d]
        ny = y + dy[d]

        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
            cleaning(nx, ny, d)
            return

    # 4방향 모두 청소 불가 → 후진
    back = (d + 2) % 4
    bx = x + dx[back]
    by = y + dy[back]

    if 0 <= bx < n and 0 <= by < m and graph[bx][by] != 1:
        cleaning(bx, by, d)

cleaning(r, c, d)
print(answer)
