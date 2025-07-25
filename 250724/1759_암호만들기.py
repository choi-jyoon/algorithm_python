from itertools import combinations

l, c = map(int, input().split())
password = list(map(str, input().split()))
#암호는 l개, 주어진 문자는 c개 , 암호는 최소 한개의 모음과 최소 두개의 자음. 사전순 정렬
password.sort()
aeiou = ['a', 'e', 'i', 'o', 'u']
a, b = [], []
combs = list(combinations(password, l))
combs.sort()
def check_pw(password):
    a, b = 0, 0
    for p in password:
        if p in aeiou:
            a+=1
        else:
            b+=1
    if a<1 or b<2:
        return False
    return True

for comb in combs:
    if check_pw(comb):
        print(''.join(comb))
        
