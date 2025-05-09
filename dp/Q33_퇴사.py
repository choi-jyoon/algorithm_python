n = int(input())
schedule = []
for i in range(n):
    t,p = map(int, input().split())
    schedule.append([t,p])

# 첫번째에는 선택 안한 경우, 두번째에는 선택한 경우 ( 날짜도 그만큼 미뤄져야됨. )
answer = [0 for _ in range(n+1)]

money = 0
for i in range(n-1,-1,-1):
    if i + schedule[i][0] <= n:
        answer[i] = max(answer[i+1], answer[i+schedule[i][0]] + schedule[i][1])
    else:
        answer[i] = answer[i+1]
        
print(answer[0])