n = int(input())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
    
from itertools import combinations

arr = [x for x in range(n)]

combs = list(combinations(arr, n//2))
ans = 1e9
for i, comb in enumerate(combs[:len(combs)//2 ]):
    start = comb
    link = combs[-(i+1)]
    
    start_skills = list(combinations(start, 2))
    link_skills = list(combinations(link, 2))
    # print(start, link)
    ss, ls = 0,0
    
    for skill in start_skills:
        ss += graph[skill[0]][skill[1]]
        ss += graph[skill[1]][skill[0]]
    for skill in link_skills:
        ls += graph[skill[0]][skill[1]]
        ls += graph[skill[1]][skill[0]]
    ans = min(ans, abs(ss-ls))
    # print(ss, ls)
print(ans)