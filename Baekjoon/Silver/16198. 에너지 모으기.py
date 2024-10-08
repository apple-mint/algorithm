# 16198. 에너지 모으기
# https://www.acmicpc.net/problem/16198

import sys
input = sys.stdin.readline

# 에너지를 모으는 함수
def gathering(n, energy):
    
    # 함수 바깥에 있는 maxx를
    # 사용하고자 global 선언
    global maxx

    # 첫번째와 마지막은 고를 수 없으므로
    # 남은 구슬의 수가 2라면 여태까지 모은 에너지 양이
    # 최댓값인지 확인하고 최댓값이라면 값을 갱신하고 종료
    if n == 2:
        maxx = max(maxx, energy)
        return

    # 첫번째와 마지막을 제외하고 구슬을 하나 선택
    for i in range(1, n-1):
        x = weight[i]

        # 선택한 구슬을 제거
        weight.pop(i)

        # 선택한 구슬 좌우에 있던
        # 구슬의 에너지를 곱해 에너지를 모으고,
        # 이후 남은 구슬들로 에너지를 모으기 위해
        # 달라진 정보를 바탕으로 gathering 함수 호출
        gathering(n-1, energy+(weight[i-1]*weight[i]))

        # 에너지를 모으는 과정이 끝나면
        # 다른 방식으로 에너지를 모으기 위해
        # 제거했던 구슬을 다시 제자리에 삽입
        weight.insert(i, x)


N = int(input().rstrip())
weight = list(map(int, input().rstrip().split()))

# 모을 수 있는 에너지의 최댓값을
# 구하기 위해 초기값 설정
maxx = 0

# 에너지를 모으기 시작
gathering(N, 0)

# 구한 모을 수 있는 에너지의 최댓값 출력
print(maxx)