n = int(input())
arr = list(map(int, input().split()))

l = 0
r = n-1

answer = -1

while l <= r:
    m = (l + r) // 2
    if arr[m] == m:
        answer = m
        break
    elif arr[m] > m:
        r = m-1
    elif arr[m] < m:
        l = m+1

print(answer)