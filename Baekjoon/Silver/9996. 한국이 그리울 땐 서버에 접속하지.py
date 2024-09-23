# 9996. 한국이 그리울 땐 서버에 접속하지
# https://www.acmicpc.net/problem/9996

import sys
input = sys.stdin.readline

N = int(input().rstrip())

# 패턴은 항상 중간에 별표(*) 하나가 있으므로
# 이를 기준으로 패턴 앞부분, 패턴 뒷부분으로 나눠줌
front, rear = input().rstrip().split('*')

for _ in range(N):
    name = input().rstrip()
    is_da = True

    # 파일 이름이 패턴보다 그 길이가
    # 길거나 같아야 하므로 이를 확인하고
    # 파일 이름이 패턴과 일치하는지 비교
    if len(front)+len(rear) <= len(name):

        # 패턴 앞부분 전체와 파일 이름의 앞부분을
        # 비교하며 일치하는지를 확인
        for j in range(len(front)):

            # 만약 다르다면 is_da를 False로 갱신하고
            # 확인하는 것을 종료
            if name[j] != front[j]:
                is_da = False
                break
            
        # 패턴 앞부분 전체와 파일 이름 앞부분이
        # 일치했다면 패턴 뒷부분 전체와 파일 이름 뒷부분도 확인
        else:

            # 만약 다르다면 is_da를 False로 갱신하고
            # 확인하는 것을 종료
            for j in range(len(rear)):
                if name[-j-1] != rear[-j-1]:
                    is_da = False
                    break
    
    # 파일 이름이 패턴보다 그 길이가 짧다면
    # 패턴과 일치하지 않으므로
    # is_da를 False로 갱신
    else:
        is_da = False
    
    # is_da의 값에 따라 적절한 값을 출력
    if is_da:
        print('DA')
    else:
        print('NE')