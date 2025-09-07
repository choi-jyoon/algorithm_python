n, m = map(int, input().split())
graph = [['' for _ in range(m)]for _ in range(n)]
for i in range(n):
    arr = input()
    for j in range(m):
        graph[i][j] = arr[j]
        
### 1~k개의 칸 뽑아서 숫자 이어붙이기 (행/열 등차수열: dr, dc는 음수부터 0 양수까지 모두 허용)
### 완전 제곱수 확인 함수 
from math import sqrt
def check(num):
    x = sqrt(num)
    if x*x == num:
        return True
    else:
        return False
    
ans = -1
for row in range(n):
    for col in range(m):
        for dr in range(-(n-1), n):
            for dc in range(-(m-1), m):
                if dr == 0 and dc == 0:
                    continue
                r, c = row, col
                num = 0
                while 0<=r <n and 0<=c <m:
                    num = num * 10 + (ord(graph[r][c]) - 48)  # 빠르게 숫자화
                    if check(num):
                        if num > ans:
                            ans = num
                    r += dr
                    c += dc

print(ans)