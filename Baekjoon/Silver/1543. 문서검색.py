# 1543. 문서검색
# https://www.acmicpc.net/problem/1543

import sys
input = sys.stdin.readline

doc = input().rstrip()
word = input().rstrip()
N = len(word)

idx = 0
cnt = 0

# 문서를 처음부터 끝까지 탐색
while idx < len(doc):

    # 검색 범위가 문서 범위 내에 있을 때
    # 시작점으로부터 찾으려는 단어의 길이만큼의 검색 범위가
    # 검색하려는 단어와 일치하다면 cnt에 1를 더하고
    # 그 단어가 끝나는 그 다음 위치로 이동
    if idx+N-1 < len(doc):
        if doc[idx:idx+N] == word:
            cnt += 1
            idx += N
        
        # 만약 아니라면 검색 시작점의 다음 위치로 이동
        else:
            idx += 1
    
    # 검색 범위가 문서 범위 밖이라면 종료
    else:
        break

print(cnt)