n, c = map(int, input().split())

homes = []
for i in range(n):
    homes.append(int(input()))
    
homes.sort()

l = homes[0]
r = homes[n-1]

while l <= r:
    m = (l + r) //2
    
    
