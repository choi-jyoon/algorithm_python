from collections import deque
f, s, g, u, d = map(int, input().split())

q = deque()
q.append((s, 0))

visited = [False] * (f+1)
find = False
while q:
    x, ans = q.popleft()
    
    if x + u == g or x - d == g:
        ans +=1
        find = True
        break
    for nx in [x+u, x-d]:
        if 0<nx<f+1 and not visited[nx]:
            visited[nx] = True
            q.append((nx, ans+1))
    
if find:       
    print(ans)
else:
    print("use the stairs")