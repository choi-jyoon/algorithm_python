n = int(input())
arr = list(map(int, input().split()))
plus, minus, multiply, divide = map(int, input().split())

def dfs(i, x, plus, minus, multiply, divide):
    global max_res
    global min_res
    
    if i == n:
        max_res = max(max_res, x)
        min_res = min(min_res, x)
        return 
    if plus > 0:
        dfs(i+1, x + arr[i], plus-1, minus, multiply, divide)
    if minus>0:
        dfs(i+1, x - arr[i], plus, minus-1, multiply, divide)
    if multiply>0:
        dfs(i+1, x * arr[i], plus, minus, multiply-1, divide)
    if divide>0:
        if x <0:
            dfs(i+1, -(-x // arr[i]), plus, minus, multiply, divide-1 )
        else:
            dfs(i+1, x//arr[i], plus, minus, multiply, divide-1)
    
max_res = -1e9
min_res = 1e9

dfs(1, arr[0], plus, minus, multiply, divide)
print(max_res)
print(min_res)