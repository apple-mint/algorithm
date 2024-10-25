# 31797. 아~파트 아파트
# https://www.acmicpc.net/problem/31797

import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

# 참가자의 두 손의 높이의 범위는
# 1부터 10,000이므로 아래와 같이 범위 설정
apt = [0] * 10001

# 손의 높이에 해당하는 인덱스에 접근해
# 해당 인덱스에 참가자의 번호를 표시
for i in range(1, M+1):
    h1, h2 = map(int, input().rstrip().split())
    apt[h1] = i
    apt[h2] = i

# N층이 될 때까지 쌓여있는 손을
# 밑에서부터 순차적으로 탐색
cnt = 0
while cnt < N:

    # 1부터 10,000의 높이 중 사람의 손이 있으면
    # 층을 하나 센 것이므로 cnt에 1을 더함
    for floor in range(10001):
        if apt[floor]:
            cnt += 1

        # 만약 그 층이 N층이라면
        # 술을 마시게 될 사람의
        # 번호를 출력하고 탐색 종료
        if cnt == N:
            print(apt[floor])
            break