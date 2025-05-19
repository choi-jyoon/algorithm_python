n = int(input())
arr = list(map(int, input().split()))
arr.sort()


m = int(input())
find = list(map(int, input().split()))

for x in find:
    # print(x)
    l = 0
    r = n
    exist = False
    while l <= r:
        mid = (l+r) // 2
        if mid >= n:
            break
        if arr[mid] < x:
            l = mid+1
        elif arr[mid] > x:
            r = mid-1
        elif arr[mid] == x:
            exist = True
            break
    if exist:
        print(1)
    else:
        print(0)
            
    