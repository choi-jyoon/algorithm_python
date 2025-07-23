from collections import deque

n, l, r = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def bfs(x, y, opened):
    q = deque()
    q.append((x, y))
    union = [(x, y)]
    opened[x][y] = True
    total_people = graph[x][y]

    while q:
        cx, cy = q.popleft()
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not opened[nx][ny]:
                if l <= abs(graph[cx][cy] - graph[nx][ny]) <= r:
                    opened[nx][ny] = True
                    q.append((nx, ny))
                    union.append((nx, ny))
                    total_people += graph[nx][ny]
    return union, total_people

days = 0

while True:
    opened = [[False]*n for _ in range(n)]
    move_flag = False  # 연합이 생겼는지 확인

    for i in range(n):
        for j in range(n):
            if not opened[i][j]:
                union, total_people = bfs(i, j, opened)
                if len(union) > 1:  # 연합이 2개 이상이면 이동 발생
                    move_flag = True
                    new_pop = total_people // len(union)
                    for ux, uy in union:
                        graph[ux][uy] = new_pop

    if not move_flag:  # 더 이상 인구 이동 없음
        break
    days += 1

print(days)

### 시간초과 dfs 문제풀이 ### 
# import sys
# sys.setrecursionlimit(10**6)

# n, l, r = map(int, input().split())
# graph = []
# for i in range(n):
#     graph.append(list(map(int, input().split())))
    

# finish = False

# dx = [-1, 0, 1, 0]
# dy = [0, -1, 0, 1]
# answer = 0
# while True:
#     opened = [[0 for _ in range(n)] for _ in range(n)]
#     people = 0
#     cnt = 0
#     def dfs(x, y, m):
#         global people, cnt
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
            
#             if 0<=nx<n and 0<=ny<n:
#                 if l <= abs(graph[x][y] - graph[nx][ny]) <=r and opened[nx][ny] ==0:
#                     # print("---", nx, ny, graph[nx][ny], graph[x][y] )
#                     if opened[x][y] ==0:
#                         opened[x][y] = m
#                         people +=graph[x][y]
#                         cnt += 1
#                     opened[nx][ny] = m
#                     people += graph[nx][ny]
#                     cnt += 1
#                     dfs(nx, ny, m)
                    
#     people_list = []
#     m = 1
    
#     for i in range(n):
#         for j in range(n):
#             people, cnt  = 0, 0
#             dfs(i, j, m)
#             # print(opened)
#             if opened[i][j] ==m:
#                 m += 1
#                 people_list.append([people, cnt])
            
#     if len(people_list)<1 or m <= 1:
#         break
#     # print(people_list, m)
#     for x in range(m-1):
#         people = people_list[x][0]
#         cnt = people_list[x][1]
#         new_people = people // cnt 
#         for i in range(n):
#             for j in range(n):
#                 if opened[i][j] == x+1:
#                     graph[i][j] = new_people
#                     opened[i][j] = 0
        
#     answer += 1

# print(answer)