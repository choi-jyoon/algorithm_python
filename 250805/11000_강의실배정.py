import heapq 
import sys 
input = sys.stdin.readline

n = int(input())
classes = []
for _ in range(n):
    s, t = map(int, input().split())
    classes.append((s, t))
    
classes.sort(key=lambda x: (x[0], x[1]))
answer = 1

rooms = []

for s, e in classes:
    if rooms and rooms[0]<= s:
        heapq.heappop(rooms)
    heapq.heappush(rooms, e)
    
print(len(rooms))