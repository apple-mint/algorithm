# 1969. DNA
# https://www.acmicpc.net/problem/1969

import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

dna = []
for _ in range(N):
    dna.append(input().rstrip())

s = ''
cnt = 0

# Hamming Distance의 합이 가장 작은 DNA s는
# 각 위치의 뉴클레오티드 문자가 전체 DNA의 해당 위치에서
# 가장 많이 나온 것으로 이루어진 DNA임
for i in range(M):
    a, c, g, t = 0, 0, 0, 0

    # 각 위치의 뉴클레오티드 문자가 무엇인지 그 수를 계산
    for num in range(N):
        if dna[num][i] == 'A':
            a += 1
        elif dna[num][i] == 'C':
            c += 1
        elif dna[num][i] == 'G':
            g += 1
        else:
            t += 1
    
    # 가장 많이 나온 뉴클레오티드 문자의 수를 찾음
    maxx = max(a, c, g, t)

    # Hamming Distance는 뉴클레오티드 문자가 다른 것의 개수이므로
    # 전체 DNA의 수에서 최댓값을 빼 더해줌
    cnt += (N-maxx)

    # 최댓값에 해당하는 뉴클레오티드 문자가
    # 무엇인지 찾고 해당 문자를 s에 더해줌
    # 사전순으로 가장 앞서는 것을
    # 출력할 수 있도록 사전순으로 if문 구현
    if maxx == a:
        s += 'A'
    elif maxx == c:
        s += 'C'
    elif maxx == g:
        s += 'G'
    else:
        s += 'T'

# 출력 예시에 따라 s, Hamming Distance의 합을 출력
print(s)
print(cnt)