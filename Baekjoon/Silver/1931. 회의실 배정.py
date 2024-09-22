# 1931. 회의실 배정
# https://www.acmicpc.net/problem/1931

import sys
input = sys.stdin.readline

N = int(input().rstrip())

info = []
for _ in range(N):
    start, end = map(int, input().rstrip().split())
    info.append((start, end))

# 회의가 빨리 끝날수록 더 많은 회의를 할 수 있으므로
# 회의의 끝나는 시간을 기준으로 오름차순 정렬
# 만약 회의의 끝나는 시간이 같을 경우 회의를 일찍 시작할수록
# 회의실이 비는 시간을 최소화하면서 더 많은 회의를 할 수 있으므로
# 회의의 시작시간을 기준으로 오름차순 정렬
info.sort(key=lambda x:(x[1], x[0]))

cnt = 0
finish = 0
for i in range(N):

    # 만약 이전 회의가 끝난 시간보다
    # 현재 회의의 시작시간이 크거나 같다면
    # 해당 회의를 할 수 있으므로 cnt에 1을 더해주고
    # 이전 회의가 끝난 시간을 현재 회의의 끝나는 시간으로 갱신
    if info[i][0] >= finish:
        cnt += 1
        finish = info[i][1]

# 회의의 최대 개수 출력
print(cnt)