# 14889. 스타트와 링크
# https://www.acmicpc.net/problem/14889

import sys, itertools
input = sys.stdin.readline

N = int(input().rstrip())
S = [list(map(int, input().rstrip().split())) for _ in range(N)]

# N명을 두 팀으로 나누는 조합을 만듦
combis = list(itertools.combinations(range(N), N//2))

# 두 팀의 능력치 차이의 최솟값을 구하기 위해
# 충분히 큰 수로 초기값 설정
ans = float('inf')

# 하나의 조합을 만들 때 각 팀에 속한 사람의 번호가
# 오름차순으로 선택되므로 각각 왼쪽, 오른쪽에서
# 하나씩 가져오면 N명을 두 팀으로 나누는 하나의 경우가 완성됨
for i in range(len(combis)//2):

    # 두 팀을 만드는 경우의 수 중 합쳤을 때
    # 0부터 N까지 모든 사람의 번호가
    # 나올 수 있도록 짝을 지음
    one = combis[i]
    two = combis[len(combis)-1-i]

    cnt1, cnt2 = 0, 0

    # 각 팀마다 서로 다른 두 명씩 선택해
    # 같은 팀에 속했을 때 팀에 더해지는 능력치를 더해줌
    for i in range(N//2-1):
        for j in range(i+1, N//2):
            oi, oj = one[i], one[j]
            ti, tj = two[i], two[j]
            
            cnt1 += S[oi][oj] + S[oj][oi]
            cnt2 += S[ti][tj] + S[tj][ti]

    # 구한 값이 두 팀의 능력치 차이의 최소값인지
    # 확인 후 그렇다면 그 값을 갱신
    ans = min(ans, abs(cnt1-cnt2))

# 두 팀의 능력치 차이의 최솟값 출력
print(ans)