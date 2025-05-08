def solution(N, stages):
    answer = []
    stages.sort()
    fail = []
    for i in range(1, N+1):
        j = 0
        while j < len(stages) and stages[j] == i:
            j += 1
        if len(stages) == 0:
            fail.append([i, 0])
        else:
            fail.append([i, j / len(stages)])
        stages = stages[j:]
    fail.sort( key = lambda x: (-x[1], x[0]))
    
    for f in fail:
        answer.append(f[0])
    return answer