# 7662. 이중 우선순위 큐
# https://www.acmicpc.net/problem/7662

import sys, collections, heapq
input = sys.stdin.readline

T = int(input().rstrip())
for _ in range(T):

    # 최솟값, 최댓값 연산을 분리하기 위해
    # min_Q, max_Q를 각각 분리해서 설정
    min_Q = []
    max_Q = []

    # 실제로 존재하는 정수를 파악하기 위해
    # cnt, nums 설정
    cnt = 0
    nums = collections.defaultdict(int)

    k = int(input().rstrip())
    for _ in range(k):
        command, n = input().rstrip().split()
        n = int(n)

        # 연산을 나타내는 문자가 'I'일 때
        # 각각 min_Q, max_Q에 최솟값, 최댓값 정렬을 유지하며
        # 정수 n을 삽입하고 그 수를 cnt와 nums에 갱신
        if command == 'I':
            heapq.heappush(min_Q, n)
            heapq.heappush(max_Q, -n)
            cnt += 1
            nums[n] += 1

        # 연산을 나타내는 문자가 'D'일 때
        # Q에 삽입된 정수가 있는지 확인 후
        # 있다면 n에 따라 적절한 연산 수행
        else:
            if cnt:

                # 최댓값을 삭제하는 연산일 경우
                # max_Q에서 최댓값을 하나 반환하고
                # 해당 값이 실제로 존재하는지 nums를 통해 확인
                if n == 1:
                    while max_Q:
                        maxx = -heapq.heappop(max_Q)

                        # 실제로 존재한다면 cnt와 nums에
                        # 상태를 갱신해주고 while문 종료
                        if nums[maxx]:
                            cnt -= 1
                            nums[maxx] -= 1
                            break
                
                # 최솟값을 삭제하는 연산일 경우
                # min_Q에서 최솟값을 하나 반환하고
                # 해당 값이 실제로 존재하는지 num을 통해 확인
                else:
                    while min_Q:
                        minn = heapq.heappop(min_Q)
                        
                        # 실제로 존재한다면 cnt와 nums에
                        # 상태를 갱신해주고 while문 종료
                        if nums[minn]:
                            cnt -= 1
                            nums[minn] -= 1
                            break

    # Q에 삽입된 정수가 없다면 'EMPTY' 출력
    if not cnt:
        print('EMPTY')

    # Q에 삽입된 정수가 하나라면
    # 최댓값, 최솟값이 동일하므로 하나의 Q만 탐색
    elif cnt == 1:

        # 실제로 존재하는 정수 하나를 찾고
        # 이를 최댓값, 최솟값으로 출력
        while min_Q:
            ans = heapq.heappop(min_Q)
            if nums[ans]:
                break
                
        print(ans, ans)

    # Q에 삽입된 정수가 2개 이상이라면
    # max_Q에서 최댓값, min_Q에서 최솟값을 탐색
    else:
        while max_Q:
            maxx = -heapq.heappop(max_Q)
            if nums[maxx]:
                break

        while min_Q:
            minn = heapq.heappop(min_Q)
            if nums[minn]:
                break
        
        # 구한 최댓값, 최솟값 출력
        print(maxx, minn)