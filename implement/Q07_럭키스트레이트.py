n = input()

length = len(n)
left, right = 0, 0
for i in range(length):
    if i <= length // 2 - 1:
        left += int(n[i])
    else:
        right += int(n[i])
if left == right:
    print("LUCKY")
else:
    print("READY")