# 10709. 기상캐스터
# https://www.acmicpc.net/problem/10709

import sys
input = sys.stdin.readline

H, W = map(int, input().rstrip().split())
sky = [list(input().rstrip()) for _ in range(H)]

# 구름이 뜨지 않을 경우 -1을 출력해야 하므로
# -1를 초기값으로 설정
ans = [[-1]*W for _ in range(H)]

# 1분마다 1킬로미터씩 동쪽으로 이동하므로
# 한 행씩 구름이 오는지를 예측
for i in range(H):

    # 마지막으로 있는 구름의 위치 초기값
    cloud = -1

    for j in range(W):

        # 만약 해당 위치에 구름이 있다면
        # cloud를 j로, 처음부터 구름이 떠 있었다는 의미로
        # ans 해당 구역의 값을 0으로 갱신
        if sky[i][j] == 'c':
            cloud = j
            ans[i][j] = 0

        # 만약 구름이 없다면 해당 위치에 구름이 오는지를 확인
        # 여태까지 구름이 오지 않았고
        # 마지막으로 있는 구름의 위치가 초기값이 아니라면
        # 1분마다 1킬로미터씩 이동하므로
        # 현재 위치에서 구름의 위치를 뺀 값으로 갱신
        else:
            if ans[i][j] == -1 and cloud != -1:
                ans[i][j] = j - cloud

# 출력 예시에 따라 출력
for i in range(H):
    print(*ans[i])