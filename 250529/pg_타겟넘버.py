def solution(numbers, target):
    answer = 0
    n = len(numbers)
    def dfs(i,x):
        nonlocal answer
        if i >=n:
            if x == target:
                answer +=1
                return True
            else:
                return False
        dfs(i+1, x+numbers[i])
        dfs(i+1, x-numbers[i])
        
    dfs(0,0)
    return answer