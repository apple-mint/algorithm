# 2805. 나무 자르기
# https://www.acmicpc.net/problem/2805

import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
trees = list(map(int, input().rstrip().split()))

# 절단기 높이 H가 될 수 있는
# 최솟값과 최댓값 설정
start = 0
end = max(trees)

# 이진 탐색 시작
while start <= end:

    # 절단기 높이 H가 될 수 있는 값의 중간값 설정
    H = (start+end)//2

    cnt = 0

    # 만약 나무가 절단기 높이보다 크다면
    # H 위의 잘린 부분을 계산해 더해줌
    for tree in trees:
        if tree > H:
            cnt += tree-H

    # 만약 자른 나무의 길이의 합이 M보다 크거나 같다면
    # 나무를 덜 잘라야 하므로 H에 1을 더해 높이를 높여줌
    if cnt >= M:
        start = H+1

    # 만약 자른 나무의 길이의 합이 M보다 작으면
    # 나무를 더 잘라야 하므로 H에 1을 더해 높이를 낮춰줌
    else:
        end = H-1

# 구한 절단기 높이 H의 최댓값 출력
print(end)