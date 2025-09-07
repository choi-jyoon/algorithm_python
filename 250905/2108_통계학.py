import sys
from collections import Counter
from decimal import Decimal, ROUND_HALF_UP

input = sys.stdin.readline

n = int(input())
nums = [int(input()) for _ in range(n)]
nums.sort()

# 1) 산술평균: half-up
s = sum(nums)
mean = int((Decimal(s) / Decimal(n)).quantize(0, rounding=ROUND_HALF_UP))

# 2) 중앙값
median = nums[n // 2]

# 3) 최빈값: 동률이면 두 번째로 작은 값
cnt = Counter(nums)
max_freq = max(cnt.values())
candidates = sorted([k for k, v in cnt.items() if v == max_freq])
mode = candidates[1] if len(candidates) > 1 else candidates[0]

# 4) 범위
rng = nums[-1] - nums[0]

print(mean)
print(median)
print(mode)
print(rng)
