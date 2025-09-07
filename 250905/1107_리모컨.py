n = int(input())
m = int(input())
broken = []
if m>0:
    broken = list(map(int, input().split()))


### 100번에서 n번으로 이동하려고 함. 고장난 버튼 제외하고 0-9 숫자 버튼과  +1/-1을 이용해서 100->n으로 가는 최단 시간
if n == 100:
    print(0)
    exit(0)

buttons = []
for i in range(10):
    if i not in broken:
        buttons.append(i)
# print(buttons)
# buttons 가지고 n과 가장 가까운 숫자로 이동하기 : 각 자릿수 비교해서 찾기 or 이분탐색이나 이런걸로 찾기 
sn = str(n)
candi = []
if len(buttons)>0:
    # for x in sn[-1::-1]:
    #     if x in buttons:
    #         candi.append(int(x))
    #     else:
    #         tmp = buttons[0]
    #         for i in buttons[1:]:
    #             if abs(int(x)-tmp) > abs(int(x)-i):
    #                 tmp = i
    #         candi.append(tmp)
        
    # can = int(''.join(map(str, reversed(candi))))
    # print(candi, can)
    
    # 자릿수 변화 x 가까운 수 찾기 
    for x in sn:
        if x in buttons:
            candi.append(int(x))
        else:
            tmp = buttons[0]
            for i in buttons[1:]:
                if abs(int(x)-tmp) > abs(int(x)-1):
                    tmp = i
            candi.append(tmp)
    can = int(''.join(map(str, reversed(candi))))
    
    # 자릿수 +1 가까운 수 찾기 
    
    ans = len(candi)
    ans += abs(can - n)
    print(ans)
else:
    print(abs(n - 100))


