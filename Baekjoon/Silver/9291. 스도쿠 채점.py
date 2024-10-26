# 9291. 스도쿠 채점
# https://www.acmicpc.net/problem/9291

import sys
input = sys.stdin.readline

# 스도쿠 판이 올바른 답인지
# 만족해야 하는 조건을 확인하는 함수
def is_correct():

    # 정수 1부터 9가 하나의 행에
    # 전부 한번씩 나오는지 확인
    for i in range(9):
        nums = [0]*9
        for j in range(9):

            # 만약 나왔던 수가 다시 나왔다면
            # 올바른 스도쿠가 아니므로 False 반환
            if nums[sudoku[i][j]-1]:
                return False

            # 여태까지 나온 적이 없다면
            # 해당 수에 한번 나왔다는 표시를 해줌
            else:
                nums[sudoku[i][j]-1] = 1
    
    # 정수 1부터 9가 하나의 열에
    # 전부 한번씩 나오는지 확인
    # 구현 방식은 위와 동일
    for j in range(9):
        nums = [0]*9
        for i in range(9):
            if nums[sudoku[i][j]-1]:
                return False
            else:
                nums[sudoku[i][j]-1] = 1
    
    # 정수 1부터 9가 각 작은 3x3 정사각형에
    # 전부 한번씩 나오는지 확인
    # 구현 방식은 위와 동일
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            nums = [0]*9
            for k in range(3):
                for l in range(3):
                    if nums[sudoku[i+k][j+l]-1]:
                        return False
                    else:
                        nums[sudoku[i+k][j+l]-1] = 1

    # 도중에 함수가 종료되지 않았다면
    # 주어진 세 가지 조건을 모두 만족했다는 것이므로
    # 올바른 스도쿠이므로 True 반환
    return True


T = int(input().rstrip())
for x in range(1, T+1):
    sudoku = [list(map(int, input().rstrip().split())) for _ in range(9)]

    # 스도쿠 판이 올바른 답인지
    # 그 결과에 따라 알맞은 답을 출력
    if is_correct():
        print(f'Case {x}: CORRECT')
    else:
        print(f'Case {x}: INCORRECT')

    # 만약 테스트 케이스가 끝나지 않은 경우
    # 빈 줄을 입력받아 테스트 케이스 사이에 빈줄이 있도록 함
    if not x == T:
        input().rstrip()