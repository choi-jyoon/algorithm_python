import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

# 상태 0: 가로, 1: 세로, 2: 대각선
moves = {
    0: [(0, 1, 0), (1, 1, 2)],          # 가로 → 가로 / 대각선
    1: [(1, 0, 1), (1, 1, 2)],          # 세로 → 세로 / 대각선
    2: [(0, 1, 0), (1, 0, 1), (1, 1, 2)]# 대각선 → 가로, 세로, 대각선
}

ans = 0

def dfs(x, y, state):
    global ans
    if x == n - 1 and y == n - 1:
        ans += 1
        return
    
    for dx, dy, new_state in moves[state]:
        nx, ny = x + dx, y + dy
        
        if 0 <= nx < n and 0 <= ny < n:
            # 이동 가능한지 체크
            if new_state == 2:  # 대각선은 세 칸이 모두 비어 있어야 함
                if graph[x][y+1] or graph[x+1][y] or graph[nx][ny]:
                    continue
            else:
                if graph[nx][ny]:
                    continue
            dfs(nx, ny, new_state)

dfs(0, 1, 0)
print(ans)
