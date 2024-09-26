# 4375. 1
# https://www.acmicpc.net/problem/4375

import sys
input = sys.stdin.readline

while True:

    # 테스트 케이스가 몇 개가 주어지는지
    # 문제에 언급되지 않았으므로
    # 주어진 테스트 케이스가 끝나면
    # while문이 종료될 수 있도록 try-except 작성
    try:
        n = int(input().rstrip())
        cnt, num = 1, 1

        # int(str(num)+'1')처럼 1로만 된 수를
        # 문자로 만들고 형변환하는 방법도 있으나
        # 4300자로 그 길이를 제한하고 있으므로
        # ValueError가 발생해 답을 구할 수 없는 경우가 존재함

        # 그러므로 num이 n으로 나누어 떨어질 때까지
        # 그 다음 자릿수에 해당하는 값을 만들어 더해줌으로써
        # 각 자릿수가 모두 1로만 이루어진 n의 배수 중
        # 가장 작은 수의 자리수를 구함
        while num % n:
            num += 10**cnt
            cnt += 1

        # 구한 답을 출력
        print(cnt)

    # 주어진 테스트 케이스가 끝났을 경우,
    # 즉 n에 입력받은 변수를 저장하는 단계에서
    # 예외가 발생했을 때 break로 while문 종료
    except:
        break