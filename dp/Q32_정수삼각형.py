n = int(input())
tree = []
triangle = []
for i in range(n):
    arr = list(map(int, input().split()))
    tree.append(arr)
    triangle.append(arr)
    
for i in range(1, n):
    for j in range(len(tree[i])):
        if j == 0:
            triangle[i][j] = triangle[i-1][j] + tree[i][j]
        if j != 0 and j != len(tree[i])-1:
            triangle[i][j] = max(triangle[i-1][j]  + tree[i][j], triangle[i-1][j-1] + tree[i][j])
        if j == len(tree[i])-1:
            triangle[i][j] = triangle[i-1][j-1] + tree[i][j]

print(max(triangle[n-1]))