# 726. Number of Atoms
# https://leetcode.com/problems/number-of-atoms/description/?envType=daily-question&envId=2024-07-14

# defaultdict: 값(value)에 초깃값을 지정하여 딕셔너리를 생성하는 모듈
# 원래 초깃값 설정 없이 연산을 하는 경우 KeyError가 발생하나
# 이를 사용 시 자동으로 초깃값을 설정해주므로 예외처리를 할 필요가 없음
# 해당 문제에서는 기존 원자의 존재 여부가 연산과정에서 중요하므로 사용
from collections import defaultdict

class Solution:
    def countOfAtoms(self, formula: str) -> str:

        # 괄호 연산 순서에 따라 값이 달라지므로 stack을 이용한 문제풀이
        # 빠른 연산을 위해 초깃값을 int를 기준으로 한 딕셔너리 생성
        stack = [defaultdict(int)]

        idx = 0
        while idx < len(formula):

            # 연산 대기
            if formula[idx] == '(':
                stack.append(defaultdict(int))
                idx += 1

            # 여태까지 스택에 쌓인 것들을 연산
            elif formula[idx] == ')':

                # 하나의 딕셔너리에 쌓인 값들을 꺼냄
                dit = stack.pop()

                # 괄호 뒤에 있는 것이 연산해야 할 수인지 아닌지를 확인
                idx += 1
                num = ''
                while idx < len(formula) and formula[idx].isdigit():
                    num += formula[idx]
                    idx += 1

                # 만약 연산해야 할 수가 괄호 뒤에 있다면
                # 해당 수를 괄호 안에 있는 원자의 수에 연산
                if num:
                    for atom in dit:
                        dit[atom] *= int(num)

                # 연산이 모두 끝났으면 다음 계산을 위해
                # 먼저 stack에 들어온 이전 딕셔너리에 값 합산
                for atom in dit:
                    stack[-1][atom] += dit[atom]

            # 만약 괄호가 아니라면 원자와 그 개수를 계산
            else:

                # 괄호가 아닌 한 숫자로 시작하는 경우는 없으므로
                # 원자의 첫 철자임을 가정하고 시작
                atom = formula[idx]

                # 그 다음이 한 원자의 다음 철자인지 확인
                idx += 1
                while idx < len(formula) and formula[idx].islower():
                    atom += formula[idx]
                    idx += 1

                # 해당 원자의 개수를 확인
                # 만약 idx가 범위 내에 있고 이것이 숫자라면
                # 나중에 int로 변환을 위해 cnt에 해당 값을 더해줌
                cnt = ''
                while idx < len(formula) and formula[idx].isdigit():
                    cnt += formula[idx]
                    idx += 1

                # 만약 cnt가 초깃값이 아니라면 1 초과,
                # 초기값이라면 1이라 표기를 하지 않은 것이므로
                # 각 값에 맞게 stack 안에 있는 딕셔너리 값에 저장
                if cnt:
                    stack[-1][atom] += int(cnt)
                else:
                    stack[-1][atom] += 1

        # 모든 계산을 끝내고 알파벳순으로 정렬
        ans_dit = dict(sorted(stack.pop().items()))

        # 주어진 값에 따라 반환
        ans = ''
        for atom in ans_dit:
            ans += atom

            # 1 초과일경우에만 숫자 추가
            if ans_dit[atom] > 1:
                ans += str(ans_dit[atom])

        return ans