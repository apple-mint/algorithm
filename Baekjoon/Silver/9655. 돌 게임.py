# 9655. 돌 게임
# https://www.acmicpc.net/problem/9655

import sys
input = sys.stdin.readline

N = int(input().rstrip())

# 항상 상근, 창영 순으로 번갈아가며
# 돌의 개수를 홀수로 가져오므로
# 상근이가 이기기 위해서는 돌의 개수가 홀수,
# 창영이가 이기기 위해서는 돌의 개수가 짝수여야 함

if N%2:
    print('SK')
else:
    print('CY')