# 26070. 곰곰이와 학식
# https://www.acmicpc.net/problem/26070

import sys
input = sys.stdin.readline

# 식권 1장으로 곰곰이에게
# 밥을 사주는 경우를 계산하는 함수
def one(gom, ticket):

    # 만약 식권이 해당 식권으로 살 수 있는 음식을
    # 먹고 싶은 곰곰이의 수보다 많거나 같을 경우
    # 식권을 식권에서 곰곰이의 수만큼 뺀 값으로,
    # 곰곰이의 수를 0으로 갱신
    if ticket >= gom:
        ticket -= gom
        gom = 0

    # 아니라면 최대한 곰곰이를 배불리 먹일 수 있도록
    # 식권을 전부 사용하고 남은 곰곰이의 수를 갱신
    else:
        gom -= ticket
        ticket = 0

    # 남은 곰곰이의 수와 식권을 반환
    return gom, ticket


# 식권 3장으로 곰곰이에게
# 밥을 사주는 경우를 계산하는 함수
# 이전 함수와 동일한 방식으로 구현
def three(gom, ticket):
    if gom and ticket//3:
        if ticket//3 >= gom:
            ticket -= 3*gom
            gom = 0
        
        else:
            gom -= ticket//3
            ticket -= 3*(ticket//3)

    return gom, ticket


# 식권 9장으로 곰곰이에게
# 밥을 사주는 경우를 계산하는 함수
# 이전 함수와 동일한 방식으로 구현
def nine(gom, ticket):
    if gom and ticket//9:
        if ticket//9 >= gom:
            ticket -= 9*gom
            gom = 0
        
        else:
            gom -= ticket//9
            ticket -= 9*(ticket//9)
    
    return gom, ticket


A, B, C = map(int, input().rstrip().split())
X, Y, Z = map(int, input().rstrip().split())

# 밥을 사주려는 곰곰이의 수를 구함
total = A+B+C

# 식권 1장으로 곰곰이에게 밥을 사준 뒤
# 아직 밥을 사주지 못한 곰곰이의 수와
# 남은 식권의 수를 갱신
A, X = one(A, X)
B, Y = one(B, Y)
C, Z = one(C, Z)

# 식권 3장으로 곰곰이에게 밥을 사준 뒤
# 아직 밥을 사주지 못한 곰곰이의 수와
# 남은 식권의 수를 갱신
A, Z = three(A, Z)
B, X = three(B, X)
C, Y = three(C, Y)

# 식권 9장으로 곰곰이에게 밥을 사준 뒤
# 아직 밥을 사주지 못한 곰곰이의 수와
# 남은 식권의 수를 갱신
A, Y = nine(A, Y)
B, Z = nine(B, Z)
C, X = nine(C, X)

# 밥을 사주려는 곰곰이의 수에서
# 밥을 사주지 못한 곰곰이의 수를 빼
# 배불리 먹일 수 있는 곰곰이의 최대 마릿수를 구하고 출력
eat = total-(A+B+C)
print(eat)