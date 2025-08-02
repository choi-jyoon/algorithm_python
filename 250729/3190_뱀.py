from collections import deque

n = int(input())
k = int(input())

graph = [[0 for _ in range(n)] for _ in range(n)]
apples = deque()
for apple in range(k):
    x,y = map(int, input().split())
    graph[x-1][y-1] = 1

l = int(input())
directions = []
for direction in range(l):
    x,c = map(str, input().split())
    directions.append((int(x), c))
    
dx = [0, 1,0, -1]
dy = [1, 0, -1, 0]



def turn(direction, c):
    if c == 'L':
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4
    return direction
        
def simulate():
    x,y = 0,0
    graph[x][y] = 2
    direction = 0
    time = 1
    index = 0
    q = [(x,y)]
    
    while True:
        nx = x + dx[direction]
        ny = y + dy[direction]
        if 0<=nx<n and 0<=ny<n and graph[nx][ny] != 2:
            if graph[nx][ny] == 0:
                graph[nx][ny] =2
                q.append((nx, ny))
                px, py = q.pop(0)
                graph[px][py] = 0
                
            if graph[nx][ny] == 1:
                graph[nx][ny] = 2
                q.append((nx, ny))
        else:
            break
        x, y = nx, ny
        time += 1
        
        if index < l and time == directions[index][0]:
            direction = turn(direction, directions[index][1])
            index += 1
    return time 

print(simulate())