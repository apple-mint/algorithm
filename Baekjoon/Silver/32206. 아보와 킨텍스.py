# 32206. 아보와 킨텍스
# https://www.acmicpc.net/problem/32206

import sys
input = sys.stdin.readline

N = int(input().rstrip())
S = input().rstrip()

# 문자열 S의 앞이나 뒤, 또는 이미 존재하는
# 두 문자 사이에 영문 소문자를 하나 넣을 경우
# 영문 소문자를 넣을 수 있는 위치에
# 해당 위치 전, 또는 후와 같은 알파벳이 들어갈 경우
# 'k'kintex, k'k'intex와 같이 같은 문자열이 발생

# 'k'kintex, k'k'intex
# k'i'intex, ki'i'ntex
# ki'n'ntex, kin'n'tex
# kin't'tex, kint't'ex
# kint'e'ex, kinte'e'x
# kinte'x'x, kintex'x'

# 다음과 같이 문자열의 길이만큼
# 중복된 문자열이 나오므로 이를 고려해야 함

# 따라서 영문 소문자를 넣을 수 있는 위치(N+1)와
# 영문 소문자의 수(26)를 곱하고 여기서 중복된 값(N)을 제거해
# 나올 수 있는 서로 다른 문자열의 개수를 구함
print(26*(N+1)-N)