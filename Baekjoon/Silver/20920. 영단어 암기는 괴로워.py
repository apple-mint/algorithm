# 20920. 영단어 암기는 괴로워
# https://www.acmicpc.net/problem/20920

import sys, collections
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

# 기본값을 0으로 하는 영어 단어장 딕셔너리 생성
voca = collections.defaultdict(int)
for _ in range(N):
    word = input().rstrip()

    # 길이가 M 이상인 단어들만 외운다고 하므로
    # 길이가 M 이상일 때 해당 단어가 나온 횟수 갱신
    if len(word) >= M:
        voca[word] += 1

# 1. 자주 나오는 단어일수록,
# 2. 해당 단어의 길이가 길수록,
# 3. 알파벳 사전 순으로 앞에 배치해야 하므로
# lambda 식을 활용해 조건에 맞춰 정렬
ans = sorted(voca.items(), key=lambda x:(-x[1], -len(x[0]), x[0]))

# 단어장의 앞에 위치한 단어부터
# 한줄에 한단어씩 출력
for word, _ in ans:
    print(word)