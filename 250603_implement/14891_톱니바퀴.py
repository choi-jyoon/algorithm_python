from math import pow

tobni = [[0 for _ in range(8)] for _ in range(4)]
for i in range(4):
    arr = input()
    for j in range(8):
        tobni[i][j] = int(arr[j])

k = int(input())
rotate = []
def rotate_tobni(tobni, n, d):
    new_tobni = [0 for _ in range(8)]
    if d == 1:
        for i in range(8):
            new_tobni[(i + 1) % 8] = tobni[n][i]
    elif d == -1:
        for i in range(8):
            new_tobni[i] = tobni[n][(i + 9) % 8]
    tobni[n] = new_tobni

for _ in range(k):
    rotate.append(list(map(int, input().split())))

for i in range(k):
    n, d = rotate[i][0], rotate[i][1]

    cascade = [False, False, False]
    if tobni[0][2] != tobni[1][6]:
        cascade[0] = True
    if tobni[1][2] != tobni[2][6]:
        cascade[1] = True
    if tobni[2][2] != tobni[3][6]:
        cascade[2] = True

    visited = [False for _ in range(4)]
    def rotate_cascade(tobni, n, d):
        rotate_tobni(tobni, n, d)
        visited[n] = True

        if n - 1 >= 0 and not visited[n - 1] and cascade[n - 1]:
            rotate_cascade(tobni, n - 1, -d)

        if n + 1 <= 3 and not visited[n + 1] and n < 3 and cascade[n]:
            rotate_cascade(tobni, n + 1, -d)

    rotate_cascade(tobni, n - 1, d)

ans = 0
for i in range(4):
    ans += tobni[i][0] * int(pow(2, i))

print(ans)
