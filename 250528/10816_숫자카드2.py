from collections import Counter

n = int(input())
cards = list(map(int, input().split()))
m = int(input())
targets = list(map(int, input().split()))

# target 에 해당하는 카드를 몇개 갖고 있는지

card_counter = Counter(cards)

for t in targets:
    print(card_counter[t], end=' ')
