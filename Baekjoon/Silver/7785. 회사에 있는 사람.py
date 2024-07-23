# 7785. 회사에 있는 사람
# https://www.acmicpc.net/problem/7785

import sys
input = sys.stdin.readline

n = int(input().rstrip())

# 빠른 탐색을 위해 사람들의 출퇴근 여부를
# 딕셔너리를 사용해 표시
company = {}

for _ in range(n):
    name, status = input().rstrip().split()

    # 만약 출근했다면 해당 이름에 1 표시
    if status == 'enter':
        company[name] = 1

    # 만약 퇴근했다면 해당 이름에 0 표시
    else:
        company[name] = 0

ans = []

# company에 저장된 사람들 이름을 기준으로 탐색
for name in company.keys():

    # 만약 그 값이 있다면 출근하고 퇴근하지 않았으므로
    # 현재 회사에 있는 사람이므로 ans에 삽입
    if company[name]:
        ans.append(name)

# 사전 순의 역순으로 출력하기 위해 내림차순 정렬
# 한 줄에 한 명씩 출력하기 위해 sep 사용
print(*sorted(ans, reverse=True), sep='\n')