n = int(input())
meetingrooms = []

for _ in range(n):
    meetingrooms.append(list(map(int, input().split())))
    
meetingrooms.sort(key = lambda x: (x[1], x[0]))

cur =meetingrooms[0]
answer = 1

for meeting in meetingrooms[1:]:
    if meeting[0]>=cur[1]:
        cur = meeting
        answer +=1
        
print(answer)