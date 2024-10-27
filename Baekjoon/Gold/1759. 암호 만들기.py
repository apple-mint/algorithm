# 1759. 암호 만들기
# https://www.acmicpc.net/problem/1759

import sys, itertools
input = sys.stdin.readline

L, C = map(int, input().rstrip().split())
alphabet = input().rstrip().split()

# combinations은 연산을 하려는 객체의 요소의 순서에 따라
# 사전식 순서로 조합 연산 결과가 나오므로
# 암호를 이루는 알파벳이 암호에서 증가하는 순서로 배열될 수 있도록
# alphabet을 오름차순 정렬하고 combinations 사용
alphabet.sort()
combis = list(itertools.combinations(alphabet, L))

# 조합 결과 중 가능성 있는 암호를 탐색
for combi in combis:
    vowel = 0
    consonant = 0

    # 모음, 자음의 개수 확인
    for i in range(L):
        if combi[i] in ('a', 'e', 'i', 'o', 'u'):
            vowel += 1
        else:
            consonant += 1
    
    # 만약 모음이 1개 이상이고 자음이 2개 이상이라면
    # 가능성 있는 암호이므로 이를 출력
    if vowel >= 1 and consonant >= 2:
        print(*combi, sep='')