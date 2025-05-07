from collections import deque

T = int(input())
for tc in range(T):
    p = input()
    n = int(input())
    xs = input()
    if len(xs) == 2:
        arr = deque([])
    else:
        arr = deque()
        for x in list(map(int, xs[1:-1].split(','))):
            arr.append(x)
    isempty = False
    reverse = False
    for x in p:
        if x == 'R':
            reverse = not reverse
        elif x == 'D' and not arr:
            isempty = True
        else:
            if reverse:
                arr.pop()
            else:
                arr.popleft()
    if isempty:
        print('error')
    else:
        if reverse:
            arr.reverse()
        print(f"[{','.join(map(str, arr))}]")