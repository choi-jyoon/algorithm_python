def solution(s):
    answer = 0
    arr = list(map(str, s.split(' ')))
    prev = 0
    for x in arr:
        if x == 'Z':
            answer -=prev
        else:
            answer += int(x)
            prev = int(x)
    # print(arr)
    return answer