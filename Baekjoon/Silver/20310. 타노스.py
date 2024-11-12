# 20310. 타노스
# https://www.acmicpc.net/problem/20310

import sys
input = sys.stdin.readline

S = input().rstrip()

# S를 구성하는 문자 중 절반의 0과 절반의 1을 제거해
# 사전순으로 가장 빠른 새로운 문자열 S'를 만들기 위해서는
# 1은 앞에서부터, 0은 뒤에서부터 제거해야 함

zero_cnt = S.count('0')//2
one_cnt = S.count('1')//2

# 해당 인덱스에 해당하는 문자가
# 제거되었는지 확인하기 위한 리스트
removed = [0] * len(S)

# 앞에서부터 절반의 1의 수만큼 1을 제거
idx = 0
while one_cnt:
    if S[idx] == '1':
        removed[idx] = 1
        one_cnt -= 1
    idx += 1

# 뒤에서부터 절반의 0의 수만큼 0을 제거
idx = len(S)-1
while zero_cnt:
    if S[idx] == '0':
        removed[idx] = 1
        zero_cnt -= 1
    idx -= 1

# 제거되지 않은 문자들을 붙여
# 새로운 문자열 S'를 만듦
ans = ''
for i in range(len(S)):
    if not removed[i]:
        ans += S[i]

# 문자열 S' 출력
print(ans)