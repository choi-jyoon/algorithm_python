n = int(input())
soldiers = list(map(int, input().split()))
answer = 0
cur = soldiers[0]
for i, power in enumerate(soldiers[1:]):
    if cur > power:
        if i != n-1:
            if cur > soldiers[i] > power:
                answer += 1
                
print(answer)