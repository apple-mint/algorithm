# 1181. 단어 정렬
# https://www.acmicpc.net/problem/1181

import sys
input = sys.stdin.readline

N = int(input().rstrip())

# 중복된 단어를 제거하기 위해 set 사용
words = set()
for _ in range(N):
    words.add(input().rstrip())

# lambda 함수를 활용해 길이가 짧은 순대로,
# 만약 길이가 같으면 그다음에는 사전 순으로 정렬되도록 함
words = sorted(words, key=lambda x:(len(x), x))

# 정렬한 단어들을 예시에 맞게 출력
print(*words, sep='\n')