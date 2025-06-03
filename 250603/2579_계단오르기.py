n = int(input())
stairs = []
for _ in range(n):
    stairs.append(int(input()))
    
score = [[] for _ in range(301)]
score[0] = [stairs[0], stairs[0]]
if n >1:
    score[1] = [stairs[1], stairs[0] + stairs[1]]

for i in range(2, n):
    score[i] = [max(score[i-2]) + stairs[i], score[i-1][0] + stairs[i]]
    
if n == 0:
    print(stairs[0])
else:
    print(max(score[n-1]))