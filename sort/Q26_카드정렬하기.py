import heapq

n = int(input())
cards = []
for i in range(n):
    cards.append(int(input()))
    
cards.sort()
heapq.heapify(cards)

answer = 0
while len(cards)>1:
    a = heapq.heappop(cards)
    b = heapq.heappop(cards)
    answer += (a+b)
    heapq.heappush(cards, a+b)
print(answer)
