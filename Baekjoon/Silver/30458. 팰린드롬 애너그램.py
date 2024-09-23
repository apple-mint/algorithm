# 30458. 팰린드롬 애너그램
# https://www.acmicpc.net/problem/30458

import sys, collections
input = sys.stdin.readline

N = int(input().rstrip())
S = input().rstrip()

# 주어진 연산을 수행해 팰린드롬이 되기 위해서는
# 문자열의 길이가 홀수일 경우
# 문자열 가운데 있는 알파벳을 제외한 나머지가,
# 문자열의 길이가 짝수일 경우
# 문자열에 있는 모든 알파벳의 수가 짝수여야 함

# 문자열에 있는 알파벳의 수를 세줌
alphabet = collections.defaultdict(int)
for i in range(N):
    alphabet[S[i]] += 1

# N이 홀수일 경우 가운데에 있는 알파벳은
# 위치를 바꿀 수 없으므로 해당 알파벳의 수에서 1을 빼줌
if N % 2:
    alphabet[S[N//2]] -= 1

# 만약 알파벳의 수가 홀수라면
# 팰린드롬으로 만들 수 없다는 의미이므로
# 'No'를 출력하고 탐색 종료
for cnt in alphabet.values():
    if cnt % 2:
        print('No')
        break

# 도중에 탐색이 끝나지 않았다면
# 팰린드롬으로 만들 수 있다는 의미이므로 'Yes' 출력
else:
    print('Yes')