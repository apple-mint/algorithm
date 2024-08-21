# 11047. 동전 0
# https://www.acmicpc.net/problem/11047

import sys
input = sys.stdin.readline

N, K = map(int, input().rstrip().split())

coin = []
for _  in range(N):
    A = int(input().rstrip())
    coin.append(A)

# 동전을 최소로 사용하면서 K로 만들기 위해서는
# 단위가 가장 큰 동전의 수를 최대한 많이 사용해야 하므로
# 오름차순으로 주어진 동전을 역순으로 탐색
ans = 0
for i in range(len(coin)-1, -1, -1):

    # 만약 해당 동전이 K값보다 작거나 같다면
    # K를 만드는 데에 그 동전이 필요하다는 의미이므로
    # 몫 나누기 연산을 통해 그 개수를 구함
    # K에 해당 동전으로 만든 값을 빼고
    # ans에 해당 동전의 개수를 더해주며 값 갱신
    cnt = 0
    if K >= coin[i]:
        cnt = K//coin[i]
        K -= coin[i]*cnt
        ans += cnt

print(ans)