# 16967. 배열 복원하기
# https://www.acmicpc.net/problem/16967

import sys
input = sys.stdin.readline

H, W, X, Y = map(int, input().rstrip().split())
B = [list(map(int, input().rstrip().split())) for _ in range(H+X)]

A = [[0]*W for _ in range(H)]

# 배열 A의 크기에 맞게 배열 B에 있는 값을
# 해당하는 i, j 값에 맞게 가져와 복원
for i in range(H):
    for j in range(W):
        A[i][j] = B[i][j]

# 배열 B로 만들면서 겹쳐진 부분의 값은
# B[i][j] = A[i][j] + A[i-X][j-Y]와 같은 식을 통해
# 만들어졌으므로 이를 활용해 겹쳐진 부분을 원래대로 복원 
for i in range(X, H):
    for j in range(Y, W):
        A[i][j] = B[i][j] - A[i-X][j-Y]

# 총 H개의 줄에 배열 A의 원소를 출력
for i in range(H):
    print(*A[i], sep=' ')