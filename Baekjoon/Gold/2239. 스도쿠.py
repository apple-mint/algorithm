# 2239. 스도쿠
# https://www.acmicpc.net/problem/2239

import sys
input = sys.stdin.readline

# python3으로는 시간초과,
# PyPy3는 통과된 코드

# 선택한 칸에 해당 숫자를
# 채울 수 있는지 확인하는 함수
def is_valid(si, sj, num):

    # 가로줄에 같은 숫자가 있는지 확인하고
    # 만약 같은 숫자가 있다면 False 반환
    for i in range(9):
        if sudoku[i][sj] == num:
            return False
    
    # 세로줄에 같은 숫자가 있는지 확인하고
    # 만약 같은 숫자가 있다면 False 반환
    for j in range(9):
        if sudoku[si][j] == num:
            return False

    # 선택한 칸이 속한 3x3 사각형에
    # 같은 숫자가 있는지 확인하고
    # 만약 같은 숫자가 있다면 False 반환
    for i in range(3):
        for j in range(3):
            if sudoku[si//3*3+i][sj//3*3+j] == num:
                return False

    # 함수가 종료되지 않았다면
    # 선택한 칸에 해당 숫자를
    # 넣을 수 있다는 의미이므로 True 반환
    return True


# 채워지지 않은 칸에 1~9까지의 숫자를
# 하나씩 채우는 것을 반복하며 답을 찾는 함수
def backtracking(cnt):
    global found_answer

    # 만약 채워지지 않은 칸을 모두 채웠다면
    # found_answer를 True로 바꿔주고
    # 9개의 줄에 9개의 숫자로 답을 출력하고 종료
    if cnt == len(arr):
        found_answer = True
        for i in range(9):
            print(*sudoku[i], sep='')            
        return

    # 만약 답을 찾았다면 탐색 종료
    if found_answer:
        return

    # 숫자가 채워지지 않은 칸 하나를 선택
    si, sj = arr[cnt][0], arr[cnt][1]
    
    # 사전식으로 앞서는 것을 먼저 찾기 위해
    # 1~9까지의 숫자를 오름차순으로 선택
    for num in range(1, 10):

        # 만약 선택한 숫자를 해당 칸에 채울 수 있다면
        # 해당 칸에 선택한 숫자를 채우고
        # 다음 채워지지 않은 칸을 채울 숫자를 찾기 위해
        # cnt에 1을 더한 값을 backtracking 함수에 전달해 호출
        if is_valid(si, sj, num):
            sudoku[si][sj] = num
            backtracking(cnt+1)

            # 해당 숫자를 넣었을 때 답을 찾지 못했으므로
            # 다른 경우의 수를 찾기 위해 해당 칸을 초기화
            sudoku[si][sj] = 0


sudoku = [list(map(int, input().rstrip())) for _ in range(9)]

# 아직 숫자가 채워지지 않은 칸을 탐색해
# 해당 칸의 좌표를 arr에 저장
arr = []
for i in range(9):
    for j in range(9):
        if not sudoku[i][j]:
            arr.append((i, j))

# 답이 여러 개일 경우 사전식으로
# 앞서는 하나만 출력하면 되므로
# 답을 하나만 찾으면 종료될 수 있도록
# 답을 찾았는지를 확인하는 변수 설정
found_answer = False

# 숫자가 채워지지 않은 칸에
# 1~9까지 숫자를 채우는 것 시작
backtracking(0)