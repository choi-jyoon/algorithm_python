n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))
st = []
ans = []
### 1~n까지의 수를 스택에 push/pop 해서 입력된 수열을 만들 수 있는지 체크 (있으면 push, pop 순서대로/ 없으면 NO)

for i in range(1, n+1):
    
    st.append(i)
    ans.append('+')
    # print(st, arr)
    while len(st)>0 and st[-1] == arr[0]:
        ans.append('-')
        st.pop(-1)
        arr.pop(0)
        
if len(arr)>0:
    print("NO")
else:
    for x in ans:
        print(x)