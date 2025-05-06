# 0,1 이면 + , 나머지 수는 * 
s = input()
ans = int(s[0])
for i, x in enumerate(s[1:]):
    if int(x) == 0 or int(x) == 1 or ans == 0 or ans == 1:
        ans = ans +  int(x)
    else: 
        ans = ans * int(x)
        
print(ans)