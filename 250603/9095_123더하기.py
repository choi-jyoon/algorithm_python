t  = int(input())
memo = [0 for _ in range(12)]

for _ in range(t):
    n = int(input())
    memo[0] = 1
    memo[1] = 2
    memo[2] = 4
    for i in range(3, n+1):
        memo[i] = memo[i-3] + memo[i-2]+memo[i-1]
    print(memo[n-1])
    
    