n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
    
# 1,2,3 번 파이프 순서대로 이동방법
move_dx = [[[0, 0], [], [0,0,1,1]], [[], [1, 2],[1,1,2,2]], [[1,2], [2,3],[1,1,2,2]]]
move_dy = [[[1, 2], [], [1,2,1,2]], [[], [0, 0], [0,1,0,1]], [[2, 3],[1,1], [1,2,1,2]]]


ans = 0
visited = [[[False, False, False] for _ in range(n)] for _ in range(n)]
def dfs(x,y, pipe):
    global ans
    if x == n-1 and y == n-1:
        graph[x][y] +=1
    for i in range(3):
        dx = move_dx[pipe]
        dy = move_dy[pipe]
        
        for j in range(3):
            nx_list = []
            ny_list = []
            for k in range(len(dx[j])):
                nx = x + dx[j][k]
                ny = y + dy[j][k]
                
                if 0<=nx <n and 0<=ny<n:
                    if graph[nx][ny] != 1:
                        nx_list.append(nx)
                        ny_list.append(ny)
            print(pipe, nx_list, ny_list)
            if len(nx_list) != 0 and len(nx_list) == len(dx[j]):
                # visited[nx][ny][j] = True
                for l in range(len(nx_list)):
                    graph[nx_list[l]][ny_list[l]] = -1
                dfs(nx_list[-1], ny_list[-1], j)

visited[0][0][0] = True
dfs(0,0, 0)
print(graph)