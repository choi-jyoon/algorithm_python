n, m = map(int, input().split())
balls = list(map(int, input().split()))

ball_dict = dict()

for i in range(n):
    ball_dict[i]=balls[i]
    
ans = 0
for i in range(n):
    for j in range(i+1, n):
        if ball_dict[i] != ball_dict[j]:
            ans +=1
print(ans)