expression = input().split('-')

# 첫 번째 항은 더해줌
result = sum(map(int, expression[0].split('+')))

# 그 이후 항은 괄호로 묶인 것처럼 모두 더한 뒤 빼줌
for part in expression[1:]:
    result -= sum(map(int, part.split('+')))

print(result)
