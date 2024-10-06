# 11656. 접미사 배열
# https://www.acmicpc.net/problem/11656

import sys
input = sys.stdin.readline

S = input().rstrip()

# S의 접미사 모음
suffix = []

# S의 길이만큼 앞에서부터 인덱스를
# 하나씩 뒤로 이동하면서 접미사를 만들고
# 해당 접미사를 suffix에 삽입
for i in range(len(S)):
    suffix.append(S[i:])

# S의 접미사를 사전순으로 정렬
suffix.sort()

# 사전순으로 정렬된 S의 접미사를
# 한 줄에 하나씩 출력
print(*suffix, sep='\n')