# 15649. N과 M (1)
# https://www.acmicpc.net/problem/15649

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

# 길이가 M인 수열을 만드는 함수
def backtracking():

    # 만약 길이가 M개인 수열이 완성되었다면
    # 리스트에 담긴 숫자들을 출력 예시에 따라 출력하고
    # 수열을 만드는 것을 종료
    if len(ans) == M:
        print(*ans, sep=' ')
        return
    
    # 사전 순으로 증가하는 순서로 출력하기 위해
    # 오름차순으로 수열을 만듦
    for num in range(1, N+1):

        # 만약 num이 ans에 없을 경우
        # 수열에 없는 숫자이므로
        # num을 삽입하고 다음 숫자를 넣을 수 있는지
        # 탐색하기 위해 backtracking 함수 호출
        if num not in ans:
            ans.append(num)
            backtracking()

            # 길이가 M개인 수열을 완성한 뒤
            # 또다른 길이가 M개인 수열을 만들고자
            # 맨 끝에 있는 숫자를 제거
            ans.pop()


N, M = map(int, input().rstrip().split())

# 길이가 M인 수열을 담을 리스트
ans = []

# 길이가 M인 수열을 만듦
backtracking()