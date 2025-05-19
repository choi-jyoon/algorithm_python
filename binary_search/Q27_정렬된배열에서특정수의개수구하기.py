n, x = map(int, input().split())
arr = list(map(int, input().split()))

l = 0
r = n-1
answer = -1

while l <= r:
    m = (l + r) // 2
    if arr[m] < x:
        l = m +1
    elif arr[m] > x:
        r= m-1
    else:
        answer += 1
        arr.pop(m)
        l = 0
        r = len(arr) - 1

print(answer)