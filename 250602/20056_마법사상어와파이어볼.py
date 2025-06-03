from collections import deque

# 방향 벡터 (상, 우상, 우, 우하, 하, 좌하, 좌, 좌상)
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

n, m, k = map(int, input().split())  # 격자 크기, 파이어볼 개수, 이동 횟수
fireballs = deque()

# 초기 파이어볼 정보 입력
for _ in range(m):
    r, c, mass, speed, direction = map(int, input().split())
    fireballs.append((r - 1, c - 1, mass, speed, direction))  # 0-indexed

for _ in range(k):
    # 1단계: 모든 파이어볼 이동
    grid = [[[] for _ in range(n)] for _ in range(n)]
    while fireballs:
        x, y, m, s, d = fireballs.popleft()
        nx = (x + dx[d] * s) % n
        ny = (y + dy[d] * s) % n
        grid[nx][ny].append((m, s, d))

    # 2단계: 파이어볼 병합 및 분리
    for i in range(n):
        for j in range(n):
            if len(grid[i][j]) == 0:
                continue
            elif len(grid[i][j]) == 1:
                fireballs.append((i, j, *grid[i][j][0]))
            else:
                total_m = sum(f[0] for f in grid[i][j])
                total_s = sum(f[1] for f in grid[i][j])
                count = len(grid[i][j])
                new_m = total_m // 5
                if new_m == 0:
                    continue
                new_s = total_s // count

                # 방향 체크: 모두 짝수 or 모두 홀수 → [0,2,4,6], 아니면 [1,3,5,7]
                dir_mod = [f[2] % 2 for f in grid[i][j]]
                if all(d == dir_mod[0] for d in dir_mod):
                    new_dirs = [0, 2, 4, 6]
                else:
                    new_dirs = [1, 3, 5, 7]

                for d in new_dirs:
                    fireballs.append((i, j, new_m, new_s, d))

# 최종 질량 합 출력
print(sum(f[2] for f in fireballs))
