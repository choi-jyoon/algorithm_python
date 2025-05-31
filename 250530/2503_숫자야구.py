from itertools import combinations

n = int(input())
baseball = []
for i in range(n):
    arr = list(map(int, input().split()))
    baseball.append(arr)
    
baseball.sort(key= lambda x: (-x[1], -x[2]))

def is_valid(num):
    snum = str(num)
    if '0' in snum:
        return False
    set_num = set(snum)
    if len(set_num) == 3:
        return True
    else:
        return False
    
def check_num(num, rule):
    ans, st, ball = str(rule[0]), rule[1], rule[2]
    
    for i in range(3):
        if ans[i] == num[i]:
            st -=1
        else:
            if num[i] in ans:
                ball -=1
    if st == 0 and ball == 0:
        return True
    else:
        return False
    
answer = 0
for num in range(123, 988):
    if is_valid(num):
        right = False
        for rule in baseball:
            if check_num(str(num), rule):
                right = True
            else:
                right = False
                break
        if right:
            answer +=1
            
    
print(answer)