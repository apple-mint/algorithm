# 9095. 1, 2, 3 더하기
# https://www.acmicpc.net/problem/9095

import sys
input = sys.stdin.readline

cnt = [0, 1, 2, 4]

# 1: 1      2: 2      3: 4
# 1         1+1       1+1+1     2+1
#           2         1+2       3
# 
# 4: 4+2+1=7
# 1+1+1+1     2+1+1       1+2+1       3+1
# 1+1+2       2+2
# 1+3
# 
# 5: 7+4+2=13
# 1+1+1+1+1     2+1+1+1     1+2+1+1     3+1+1
# 1+1+2+1       2+2+1       1+3+1+1
# 1+1+1+2       1+2+2       2+1+2       3+2
# 1+1+3         2+3

# 다음과 같이 하나하나 계산해본 결과
# cnt[N] = cnt[N-1] + cnt[N-2] + cnt[N-3]와 같은
# 점화식을 도출할 수 있으므로
# n의 범위인 10까지 해당 값을 계산해 저장
for num in range(4, 11):
    cnt.append(cnt[num-1]+cnt[num-2]+cnt[num-3])

T = int(input().rstrip())
for _ in range(T):
    n = int(input().rstrip())
    print(cnt[n])