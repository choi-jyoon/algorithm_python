n = int(input())
arr = list(map(int, input().split()))

lis = [1] * n
arr2 = [-1] * n
answer = []
for i in range(n):
    for j in range(i):
        if arr[j] < arr[i] and lis[j] + 1 > lis[i]:
            lis[i] = max(lis[j]+1, lis[i])
            arr2[i] = j

i = lis.index(max(lis))
while arr2[i] != -1:
    i = arr2[i]
print(arr, lis, arr2)