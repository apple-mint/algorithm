# 카펫
# https://school.programmers.co.kr/learn/courses/30/lessons/42842

def solution(brown, yellow):

    # 카펫의 가로, 세로를 x, y라고 했을 때
    # 다음과 같은 두 방정식을 세울 수 있음
    # 1. 2*(x+y-2) = brown
    # 2. (x-2)*(y-2) = yellow
    # 이를 이용해 해당 방정식을 만족하는 해를 찾아줌
    x = 1
    while True:
        if x*(brown-2*x+4) == 2*(brown+yellow):
            break
        x += 1
    
    y = (brown+yellow)//x
    
    # 가로, 세로 순으로 배열에 담아야 하고
    # 가로 길이가 세로 길이와 같거나 기므로
    # x, y 중 큰 것부터 배열에 삽입
    answer = []
    if x >= y:
        answer.append(x)
        answer.append(y)
    else:
        answer.append(y)
        answer.append(x)

    return answer