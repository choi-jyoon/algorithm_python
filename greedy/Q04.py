from itertools import combinations

n = int(input())
coins = list(map(int, input().split()))
coins.sort()

prods = []
for i in range(1, n+1):
    prods.append(list(combinations(coins, i)))

ans = 1
ans_arr = []
for prod in prods:
    for arr in prod:
        ans_arr.append(sum(arr))
     
   
ans_arr.sort()   

for i, x in enumerate(ans_arr):
    if x - ans == 1 or x == ans:
        ans = x
    else:
        print(ans+1)
        break