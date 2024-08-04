# 5430. AC
# https://www.acmicpc.net/problem/5430

import sys, collections
input = sys.stdin.readline

T = int(input().rstrip())
for _ in range(T):
    p = input().rstrip()
    n = int(input().rstrip())

    # 정수가 배열에 들어있는 정수 형태의 문자열이므로
    # 좌우 [, ]를 제거해 저장
    nums = input().rstrip()[1:-1]

    # 만약 배열에 정수가 있다면 ,를 기준으로 분리해 저장
    # 첫번째 수를 버리는 연산을 해야 하므로
    # popleft 메서드 사용이 가능한 deque 사용
    if n:
        arr = collections.deque(nums.split(','))

    # 정수가 없는 경우 빈 리스트로 저장
    else:
        arr = []

    # 수행할 함수 인덱스를 가리키는 정수
    idx = 0

    # 배열에 있는 수가 뒤집혔는지 아닌지를 확인하는 변수
    is_reverse = False

    # 빈 배열에서 D를 사용했는지 확인하는 변수
    error = False

    # 수행할 함수 수행
    while idx < len(p):

        # 만약 첫번째 수를 버리는 함수일 경우
        if p[idx] == 'D':

            # 빈 배열이 아닐 경우 뒤집혔는지 아닌지 확인 후
            # 첫번째 수를 버릴 수 있도록 적절한 메서드 사용
            if arr:
                if is_reverse:
                    arr.pop()
                else:
                    arr.popleft()

            # 만약 빈 배열일 경우 error 표시 후
            # 더이상 함수를 수행할 필요가 없으므로 종료
            else:
                error = True
                break
        
        # 만약 순서를 뒤집는 함수일 경우
        # 첫번째 수를 버리는 함수가 나올 때까지
        # 그 함수가 얼마나 나오는지를 확인
        else:
            cnt = 1
            if idx+1 < len(p) and p[idx+1] == 'R':
                cnt += 1
                idx += 1
            
            # 만약 홀수라면 해당 함수가 실행되어야 하므로
            # 현 상태가 뒤집혀있는지를 확인 후 상태 변경
            if cnt % 2:
                if is_reverse:
                    is_reverse = False
                else:
                    is_reverse = True

        # 해당 함수를 수행했다면
        # 다음 함수를 수행할 수 있도록 idx에 1를 더해줌
        idx += 1

    # 모든 함수 수행 후 에러 상태 확인
    # 만약 에러일 경우 error 출력
    if error:
        print('error')

    # 만약 정상적으로 함수가 수행되었을 경우
    # 뒤집혀있는지 상태에 따라 뒤집기 연산을 하고
    # 제시된 출력 형태에 따라 배열을 출력
    else:
        if is_reverse:
            arr = reversed(arr)

        print('[', end='')
        print(*arr, sep=',', end='')
        print(']')