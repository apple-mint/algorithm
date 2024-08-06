# 1063. 킹
# https://www.acmicpc.net/problem/1063

import sys
input = sys.stdin.readline

# 킹이 움직일 수 있는 방향을 딕셔너리 형태로 저장
move = {
    'R':(0, 1), 'L':(0, -1), 'B':(1, 0), 'T':(-1, 0),
    'RT':(-1, 1), 'LT':(-1, -1), 'RB':(1, 1), 'LB':(1, -1)
}

king, stone, N = input().rstrip().split()

# 입력받은 킹과 돌의 위치를 움직이기 편하도록
# 8x8 크기의 0~7까지의 범위 내 좌표값에 맞춰 변경

# i: 행의 가장 위를 0으로 바꾸기 위해
# 8에 주어진 값을 정수로 변환하고 빼줌
ki = 8-int(king[1])
si = 8-int(stone[1])
  
# j: 알파벳을 유니코드 코드 포인트를 나타내는 정수로 바꾸고
# 열의 가장 위를 0으로 바꾸기 위해 시작점인 A의 정수값인 65를 빼줌
kj = ord(king[0])-65
sj = ord(stone[0])-65

for _ in range(int(N)):

    # 킹의 움직임에 해당하는 좌표값을 찾아와
    # 킹이 움직일 방향 설정
    command = input().rstrip()
    i, j = move[command]

    # 킹이 도착할 위치가 체스판 범위 내에 있을 때,
    if 0<=ki+i<8 and 0<=kj+j<8:

        # 만약 도착할 위치에 돌이 있다면,
        if ki+i==si and kj+j==sj:

            # 돌을 킹의 움직임과 같게 움직였을 때
            # 체스판 범위 내에 있다면
            # 킹은 돌이 있던 위치로,
            # 돌은 킹의 움직임과 같게 이동
            if 0<=si+i<8 and 0<=sj+j<8:
                ki, kj = si, sj
                si, sj = si+i, sj+j

        # 돌이 없다면 주어진 방향대로 킹을 움직임
        else:
            ki, kj = ki+i, kj+j

# 주어진 체스판에 맞게 i, j좌표 값을 바꿔 출력
print(chr(kj+65), 8-ki, sep='')
print(chr(sj+65), 8-si, sep='')