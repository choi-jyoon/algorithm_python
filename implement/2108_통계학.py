from collections import Counter

n = int(input())
nums = []
sum_num = 0
cnt_num = dict()

for i in range(n):
    num = int(input())
    nums.append(num)
    
    sum_num+=num
    
        
nums.sort()

counter = Counter(nums)
most = counter.most_common()

if most[0][1] == most[1][1]:
    mfv=most[1][0]
else:
    mfv=most[0][0]
    
print(int(round(sum_num / n, 0)))
print(nums[n//2])
print(mfv)
print(abs(nums[-1]- nums[0]))
    
