# 4949. 균형잡힌 세상
# https://www.acmicpc.net/problem/4949

import sys
input = sys.stdin.readline

while True:
    word = input().rstrip()

    # 입력 맨 마지막에 온점 하나('.')가 들어오므로
    # 온점 하나일 경우 입력을 받는 것을 종료
    if word == '.':
        break

    # 소괄호, 대괄호를 담을 stack
    stack = []

    # 균형잡힌 문자열인지 아닌지 판단하는 변수
    is_balance = False

    # 균형잡힌 문자열인지 아닌지
    # 문자열 전체를 하나하나 탐색
    for i in range(len(word)):

        # 괄호의 시작인 '(', '[' 일 경우
        # 해당 괄호를 stack에 삽입
        if word[i] == '(' or word[i] == '[':
            stack.append(word[i])
        
        # ')'일 경우 stack에 마지막으로 들어온 괄호가
        # '('이여야 해당 괄호와 짝을 이룰 수 있으므로
        # 해당 경우를 모두 만족하지 않으면
        # 균형잡힌 문자열이 될 수 없으므로 탐색 종료
        elif word[i] == ')':
            if not stack:
                break
            x = stack.pop()
            if x != '(':
                break
        
        # ']'일 경우 stack에 마지막으로 들어온 괄호가
        # '['이여야 해당 괄호와 짝을 이룰 수 있으므로
        # 해당 경우를 모두 만족하지 않으면
        # 균형잡힌 문자열이 될 수 없으므로 탐색 종료
        elif word[i] == ']':
            if not stack:
                break
            x = stack.pop()
            if x != '[':
                break

    # 문자열을 끝까지 탐색했을 때 stack이 비어 있다면
    # 모든 괄호가 짝지어졌거나 괄호가 없는 경우로
    # 균형잡힌 문자열이므로 is_balance를 True로 갱신
    else:
        if not stack:
            is_balance = True

    # is_balance 값에 따라 적절한 문구 출력
    if is_balance:
        print('yes')
    else:
        print('no')