# 2644. 촌수계산
# https://www.acmicpc.net/problem/2644

import sys, collections
input = sys.stdin.readline

# 두 사람의 촌수를 계산하기 위해
# 두 사람의 최단거리를 구하는 bfs 함수 구현
def bfs(num1, num2):
    qu = collections.deque()

    # 친척 관계가 전혀 없어 촌수를 계산할 수 없을 때
    # -1을 출력해야 하므로 초기값을 -1로 설정
    visitied = [-1] * (n+1)
    
    # 두 사람 중 한 명의 정보를
    # bfs를 시작하기 위한 초기값으로 설정
    qu.append(num1)
    visitied[num1] = 0

    # bfs 시작
    while qu:
        people = qu.popleft()

        # 만약 bfs를 통해 다른 한 명을
        # 찾았을 경우 bfs 종료
        if people == num2:
            break
        
        # 연결된 사람들 중 아직 친척 관계를
        # 확인하지 않은 사람이 있다면
        # 연결된 또다른 친척 관계가 있는지
        # 확인하기 위해 qu에 해당 번호를 삽입하고
        # 이전 값에 1을 더한 값을 visited에 갱신해 촌수를 계산
        for p in family[people]:
            if visitied[p] == -1:
                qu.append(p)
                visitied[p] = visitied[people] + 1

    # 계산된 촌수를 반환
    return visitied[num2]


n = int(input().rstrip())
p1, p2 = map(int, input().rstrip().split())
m = int(input().rstrip())

# 주어진 부모 자식간의 관계로
# 가족 관계가 어떻게 연결되었는지를 저장
family = [[] for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, input().rstrip().split())
    family[x].append(y)
    family[y].append(x)

# 입력에서 요구한 두 사람의 촌수를
# bfs를 통해 구하고 이를 출력
print(bfs(p1, p2))