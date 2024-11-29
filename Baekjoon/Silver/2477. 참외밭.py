# 2477. 참외밭
# https://www.acmicpc.net/problem/2477

import sys
input = sys.stdin.readline

K = int(input().rstrip())

sides = []
x = []
y = []

for _ in range(6):
    num, length = map(int, input().rstrip().split())
    sides.append((num, length))

    # 만약 동쪽 또는 서쪽으로 이동했을 경우
    # 해당 변은 가로이므로 x에 해당 길이 삽입
    if num == 1 or num == 2:
        x.append(length)

    # 그렇지 않다면 해당 변은 세로이므로
    # y에 해당 길이 삽입
    else:
        y.append(length)

# 육각형의 빈 공간을 이어 사각형 모양을 만들어
# 큰 사각형 넓이 - 작은 사각형 넓이로 참외밭의 넓이를 구함

# 큰 사각형의 가로, 세로는
# 가로, 세로 각각 길이 중 가장 긴 값이므로
# max 함수를 통해 해당 값을 구해줌
large_x, large_y = max(x), max(y)

# 육각형의 모양은 ㄱ모양을 0도, 90도, 180도, 270도 회전한 모양이고
# 임의의 한 꼭짓점에서 출발해 반시계방향으로 둘레를 도므로
# ㄱ모양을 0도, 90도로 회전한 모양일 때
# 방향이 3131이 반복될 때 작은 사각형의 길이를,
# ㄱ모양을 180도, 270도로 회전한 모양일 때는
# 방향이 4242가 반복될 때 작은 사각형의 길이를 찾을 수 있음

# 따라서 방향과 길이를 요소로 가진 sides를
# 원형 큐처럼 탐색하면서 해당 x, y값을 찾음
small_x, small_y = 0, 0
for i in range(6):

    # 같은 방향이 하나의 간격을 두고 반복되었을 때,
    if sides[i][0] == sides[(i+2)%6][0]:

        # 만약 해당 방향이 가로에 해당되는 방향이라면
        # 그 사이에 세로에 해당하는 변이 있으므로
        # 해당 길이를 small_y 값으로 갱신
        if sides[i][0] == 1 or sides[i][0] == 2:
            small_y = sides[(i+1)%6][1]

        # 만약 해당 방향이 세로에 해당되는 방향이라면
        # 그 사이에 가로에 해당하는 변이 있으므로
        # 해당 길이를 small_x 값으로 갱신
        else:
            small_x = sides[((i+1)%6)][1]

# 구한 값을 바탕으로 참외밭의 넓이를 구하고
# 참외의 개수를 곱해 참외밭에서 자라는 참외의 수를 출력
print((large_x*large_y - small_x*small_y) * K)