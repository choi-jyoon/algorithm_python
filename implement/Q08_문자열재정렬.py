s = input()

strs = ''
nums = 0
for x in s:
    if x.isalpha():
        strs+=x
    else:
        nums += int(x)
answer = sorted(strs)
answer+=str(nums)
print(''.join(answer))