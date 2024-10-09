# 1138. 한 줄로 서기
# https://www.acmicpc.net/problem/1138

import sys
input = sys.stdin.readline

N = int(input().rstrip())
people = list(map(int, input().rstrip().split()))

ans = [0] * N
for i in range(N):

    # 자기보다 큰 사람이 들어갈
    # 위치의 수를 확인하기 위한 변수
    cnt = 0

    # 자기보다 큰 사람이 들어갈 위치가 있는지 확인
    for j in range(N):

        # 만약 해당 위치가 비어 있고,
        # 왼쪽에 자기보다 큰 사람이 들어갈 위치의 수를
        # 확보했다면 해당 위치에 줄을 서게 하고 종료
        if not ans[j] and cnt == people[i]:
            ans[j] = i+1
            break

        # 위치가 비어 있다면 자기보다 큰 사람이
        # 들어갈 수 있으므로 cnt에 1을 더해줌
        elif not ans[j]:
            cnt += 1

print(*ans)