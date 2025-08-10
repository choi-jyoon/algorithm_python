from collections import deque

n, k = map(int, input().split())
belt = deque(map(int, input().split()))
robot = deque([False] * (2 * n))

step = 0
while True:
    step += 1

    # 1) 벨트와 로봇 함께 회전
    belt.rotate(1)
    robot.rotate(1)
    robot[n-1] = False  # 내리는 위치 비우기

    # 2) 로봇 이동 (뒤에서 앞으로)
    for i in range(n-2, -1, -1):
        if robot[i] and not robot[i+1] and belt[i+1] > 0:
            robot[i] = False
            robot[i+1] = True
            belt[i+1] -= 1
    robot[n-1] = False  # 내리는 위치 비우기

    # 3) 올리는 위치에 로봇 올리기
    if belt[0] > 0 and not robot[0]:
        robot[0] = True
        belt[0] -= 1

    # 4) 종료 조건
    if belt.count(0) >= k:
        print(step)
        break
