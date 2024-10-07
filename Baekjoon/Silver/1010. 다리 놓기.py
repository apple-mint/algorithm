# 1010. 다리 놓기
# https://www.acmicpc.net/problem/1010

import sys, math
input = sys.stdin.readline

T = int(input().rstrip())
for _ in range(T):
    N, M = map(int, input().rstrip().split())

    # 다리를 서쪽의 사이트 개수 N만큼 지으려 하고
    # 동쪽의 사이트 개수 M은 항상 N보다 크거나 같으므로
    # 동쪽에서 서쪽 사이트 모두를 잇는 조합을 구하면 됨

    # 조합의 경우 순서 상관없이 M에서 N개를 선택하므로
    # 선택된 사이트를 오름차순으로 정렬한다면
    # 다리끼리 서로 겹쳐지지 않게 다리를 지을 수 있음

    ans = math.factorial(M) // math.factorial(M-N) // math.factorial(N)
    print(ans)