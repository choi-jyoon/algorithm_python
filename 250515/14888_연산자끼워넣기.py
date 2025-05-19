n = int(input())
arr = list(map(int, input().split()))
op_num = list(map(int, input().split()))
op = []

op.append('+') * op_num[0]
op.append('-') * op_num[1]
op.append('*') * op_num[2]
op.append('/') * op_num[3]

 
