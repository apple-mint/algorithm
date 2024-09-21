# 2630. 색종이 만들기
# https://www.acmicpc.net/problem/2630

import sys
input = sys.stdin.readline

# 전체 종이가 모두 같은 색으로 칠해져 있는지 확인하고
# 그렇지 않다면 모두 같은 색이 되거나
# 하나의 정사각형 칸이 될 때까지 종이를 자르며
# 전체 종이가 모두 같은 색인 색종이의 개수를 구하는 함수
def cut(si, sj, n):

    # global 선언으로
    # 함수 외부에 있는 white, blue에
    # 접근할 수 있도록 해 색종이의 개수를 기록
    global white, blue

    # 가장 왼쪽 상단을 기준점으로 잡고
    # 해당 종이의 색을 확인
    color = paper[si][sj]

    # 만약 전체 종이 중 기준색과 다른 곳이 있다면
    # 가로와 세로로 중간 부분을 잘라 4개로 만들고,
    # 만든 종이들이 모두 같은 색으로 칠해져 있는지 확인하고자
    # 해당 종이의 가장 왼쪽 상단 좌표,
    # 한 변의 길이를 넣어 cut 함수 실행
    for i in range(si, si+n):
        for j in range(sj, sj+n):
            if paper[i][j] != color:
                cut(si, sj, n//2)
                cut(si, sj+n//2, n//2)
                cut(si+n//2, sj, n//2)
                cut(si+n//2, sj+n//2, n//2)
                return

    # 만약 전체 종이가 모두 같은 색일 경우
    # 해당 색종이의 색에 따라 알맞은 변수에 1을 더해줌
    if not color:
        white += 1
    else:
        blue += 1
    
    return


N = int(input().rstrip())
paper = [list(map(int, input().rstrip().split())) for _ in range(N)]

white = 0
blue = 0

# NxN 크기 색종이의 가장 왼쪽 상단 좌표와
# 색종이 한 변의 길이인 N을 넣어 cut 함수 실행
cut(0, 0, N)

# 햐얀색 색종이의 개수,
# 파란색 색종이의 개수를 출력
print(white)
print(blue)