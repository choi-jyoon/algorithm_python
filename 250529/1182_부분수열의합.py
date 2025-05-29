from itertools import combinations

n, s = map(int, input().split())
arr = list(map(int, input().split()))
answer = 0


combs = []
for i in range(1, n+1):
    combs.append(list(combinations(arr, i)))

for comb in combs:
    for c in comb:
        if sum(c) == s:
            answer +=1
print(answer)