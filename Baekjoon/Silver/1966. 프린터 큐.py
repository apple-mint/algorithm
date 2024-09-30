# 1966. 프린터 큐
# https://www.acmicpc.net/problem/1966

import sys, collections
input = sys.stdin.readline

T = int(input().rstrip())

for _ in range(T):
    N, M = map(int, input().rstrip().split())
    qu = collections.deque(map(int, input().rstrip().split()))

    # 1~9까지의 중요도를 가진 문서가
    # 몇 개 있는지 확인하기 위한 딕셔너리
    docs = collections.defaultdict(int)

    # 1~9까지 중요도에 해당하는 문서가
    # 몇 개 있는지 그 수를 세주고
    # 몇 번째로 인쇄되었는지 궁금한 문서가 무엇인지
    # 확인하기 위해 문서의 인덱스를 추가해 qu 갱신
    for i in range(N):
        docs[qu[i]] += 1
        qu[i] = (qu[i], i)

    # 현재 가장 높은 중요도가 무엇인지 확인
    maxx = max(docs)

    # 문서가 몇 번째로 인쇄되는지 탐색 시작
    cnt = 0
    while qu:

        # 문서의 중요도와 인덱스 확인
        doc, idx = qu.popleft()

        # 만약 현재 문서의 중요도와
        # 가장 높은 중요도가 같은 경우 인쇄할 수 있음
        if doc == maxx:

            # 인쇄했다는 의미로 cnt에 1을 더해주고
            # docs[doc]에 해당하는 값에서 1을 빼줌
            cnt += 1
            docs[doc] -= 1

            # 만약 인쇄한 문서가 몇 번째로 인쇄되었는지
            # 궁금한 문서일 경우 탐색 종료
            if idx == M:
                break

            # 만약 가장 높은 중요도의 마지막 문서였다면
            # 그 다음 중요도가 높은 문서를 인쇄하기 위해
            # 해당 중요도를 key으로 가지는 값을 삭제하고
            # key를 기준으로 최댓값을 구해 maxx를 갱신
            if not docs[doc]:
                del docs[doc]
                maxx = max(docs)

        # 만약 같지 않다면 현재 문서보다
        # 중요도가 높은 문서가 하나라도 있다는 것이므로
        # 인쇄하지 않고 qu에 가장 뒤에 다시 재배치
        else:
            qu.append((doc, idx))

    # 문서가 몇 번째로 인쇄되었는지 출력
    print(cnt)