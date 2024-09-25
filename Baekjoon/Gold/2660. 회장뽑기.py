# 2660. 회장뽑기
# https://www.acmicpc.net/problem/2660

import sys, collections
input = sys.stdin.readline

# 몇 단계를 거쳐야 모든 회원과 친구가 되는지에 따라
# 회원의 점수가 결정되므로 bfs를 통해 이를 계산
def bfs(member):

    qu = collections.deque()
    scores = [-1] * (N+1)
 
    # 시작점이 되는 회원을 qu에 삽입하고
    # 시작한다는 의미로 단계를 0으로 설정
    qu.append(member)
    scores[member] = 0

    # bfs 시작
    while qu:

        # 기준이 되는 회원번호
        start = qu.popleft()

        # 만약 기준이 되는 회원의 친구 중
        # 아직 확인하지 못한 회원이 있다면
        # qu에 해당 회원번호를 삽입하고
        # 몇 단계를 거쳐 방문했는지 기존값에 1을 더해 갱신
        for friend in info[start]:
            if scores[friend] == -1:
                qu.append(friend)
                scores[friend] = scores[start] + 1

    # 시작점을 기준으로 마지막에 도달한 사람의 단계가
    # 그 회원의 점수가 되므로 최댓값을 반환
    return max(scores)


N = int(input().rstrip())
info = [[] for _ in range(N+1)]

# 어떤 회원끼리 친구인지 입력을 받음
while True:    
    m1, m2 = map(int, input().rstrip().split())

    # 마지막 줄이면 -1, -1이므로
    # 어떤 회원끼리 친구인지 표시하는 것을 종료
    if m1 == -1 and m2 == -1:
        break
    
    # 어떤 회원끼리 친구인지 표시
    info[m1].append(m2)
    info[m2].append(m1)

# 회장 후보의 점수 초기값 설정
minn = float('inf')

# 각 회원마다 점수가 몇 점인지를 기록할 리스트
scores = [0] * (N+1)

# 각 회원의 점수를 계산
for member in range(1, N+1):

    # bfs로 회원의 점수 계산
    score = bfs(member)

    # 해당 회원의 점수가 최솟값일 경우 최솟값 갱신
    minn = min(minn, score)

    # 최솟값인지 아닌지에 따라
    # 관계없이 점수 기록
    scores[member] = score

# 회장 후보의 점수와 후보의 수 출력
print(minn, scores.count(minn))

# 회장 후보를 오름차순으로 출력하기 위해
# 오름차순으로 각 회원의 점수가 몇 점인지 확인
# 회원의 점수가 회장 후보의 점수와 같을 경우
# 회장 후보이므로 그 회원번호를 출력
for member in range(1, N+1):
    if scores[member] == minn:
        print(member, end=' ')