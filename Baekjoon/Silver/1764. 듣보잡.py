# 1764. 듣보잡
# https://www.acmicpc.net/problem/1764

import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

# 듣보잡은 듣도 못한 사람, 보도 못한 사람 명단에
# 모두 있어야 하므로 탐색 속도를 위해 딕셔너리를 활용해
# 듣도 못한 사람의 명단을 만듦
names = {}
for _ in range(N):
    names[input().rstrip()] = 1

ans = []
for _ in range(M):
    name = input().rstrip()

    # 만약 해당 이름이 있을 경우
    # 듣보잡 명단에 추가
    if names.get(name):
        ans.append(name)

# 사전순 정렬을 위해 오름차순 정렬 후
# 제시된 출력 양식에 맞게 출력
ans.sort()
print(len(ans), *ans, sep='\n')