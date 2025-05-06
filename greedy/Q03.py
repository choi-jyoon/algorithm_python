s = input()
new_s = [s[0]]

for i, x in enumerate(s[1:]):
    if x != new_s[-1]:
        new_s.append(x)
cnt_0, cnt_1 = 0, 0
for i, x in enumerate(new_s):
    if x == '0':
        cnt_0+=1
    elif x == '1':
        cnt_1 += 1
answer = min(cnt_0, cnt_1)
print(answer)