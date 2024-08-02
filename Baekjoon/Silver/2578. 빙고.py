# 2578. 빙고
# https://www.acmicpc.net/problem/2578

import sys
input = sys.stdin.readline

# 사회자가 부른 수가 빙고판에 어디 있는지를 확인
def check_num(num):
    for i in range(5):
        for j in range(5):

            # 만약 사회자가 부른 수이면 구분을 위해
            # 1~25 범위에 해당되지 않은 0으로 값 갱신
            if bingo[i][j] == num:
                bingo[i][j] = 0

    return


# 사회자가 부른 수들을 지웠을 때
# 몇 개의 줄이 생기는지 확인
def check_bingo():
    cnt = 0

    # 가로줄에 있는 5개 모든 수가 지워지는지 확인
    for i in range(5):
        for j in range(5):
            if bingo[i][j]:
                break
        
        # 지워졌다면 그 한 줄을 cnt에 추가
        else:
            cnt += 1

    # 세로줄에 있는 5개 모든 수가 지워지는지 확인
    for j in range(5):
        for i in range(5):
            if bingo[i][j]:
                break

        # 지워졌다면 그 한 줄을 cnt에 추가
        else:
            cnt += 1

    # 왼쪽 대각선줄에 있는 5개 모든 수가 지워지는지 확인
    for i in range(5):
        if bingo[i][i]:
            break

    # 지워졌다면 그 한 줄을 cnt에 추가
    else:
        cnt += 1

    # 오른쪽 대각선줄에 있는 5개 모든 수가 지워지는지 확인
    for i in range(5):
        if bingo[i][4-i]:
            break

    # 지워졌다면 그 한 줄을 cnt에 추가
    else:
        cnt += 1

    # 지워진 줄의 수를 반환
    return cnt


bingo = [list(map(int, input().rstrip().split())) for _ in range(5)]
nums = [list(map(int, input().rstrip().split())) for _ in range(5)]

# cnt: 사회자가 부른 숫자의 수
cnt = 0

# is_bingo: 빙고인지 아닌지 상태를 확인하는 변수
# 도중에 빙고가 나올 경우 탐색을 멈추기 위해 사용
is_bingo = False

# 사회자가 말한 숫자 순대로 탐색 시작
for i in range(5):
    if not is_bingo:
        for j in range(5):

            # 사회자가 말한 숫자를 check_num 함수를 통해
            # 빙고판에서 찾고 cnt에 1 추가
            num = nums[i][j]
            check_num(num)
            cnt += 1

            # cnt가 최소 5 이상이 되어야
            # 줄을 생겼는지를 파악하는 것이 의미가 있으므로
            # cnt가 5 이상일 때부터 check_bingo 함수를 통해
            # 줄이 몇 개 생겼는지를 확인
            if cnt >= 5:

                # 만약 3개 이상의 줄이 생겼다면
                # 빙고라고 외칠 수 있으므로
                # is_bingo를 True로 갱신 후 탐색 종료
                if check_bingo() >= 3:
                    is_bingo = True
                    break

# 몇 번째 수에 빙고를 외쳤는지를 출력
print(cnt)