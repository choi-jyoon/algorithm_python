n = int(input())
podos = []
for _ in range(n):
    podos.append(int(input()))
    
taste = [[] for _ in range(100001)]

taste[0] = [podos[0], podos[0]]
max_podo = podos[0]

if n >1:
    taste[1] = [podos[1], max(taste[0]) + podos[1], max(taste[0])]
    max_podo = max(max_podo, max(taste[1]))
    
for i in range(2, n):
    taste[i] = [max(taste[i-2]) + podos[i], taste[i-1][0] + podos[i], max(taste[i-1])]
    max_podo = max(max_podo, max(taste[i]))
    
print(max_podo)
