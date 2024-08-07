# 가장 큰 수
# https://school.programmers.co.kr/learn/courses/30/lessons/42746

def solution(numbers):

    # 가장 큰 수를 만들기 위해서는
    # 단위 수가 큰 순대로 각 자릿수의 수가 커야 하므로
    # 사전순 정렬을 위해 문자열로 변환
    numbers = list(map(str, numbers))

    # [3, 30, 34] 가 있을 때 주어진 수로 정렬할 경우
    # [34, 30, 3] 이 되는데 가장 큰 수를 만들기 위해서는
    # 뒤에 바로 다른 숫자를 붙일 수 있는 3이 30보다 커야 함
    # 즉 [34, 3, 30] 으로 정렬되어야 함
    
    # 요소 범위가 0~1,000라는 것을 고려해 3을 곱한 결과로 내림차순 정렬
    # 이렇게 하면 [343434, 303030, 333] 형태로 만들어져
    # 30과 3을 비교할 때 십의 자리에서 0, 3을 비교하게 되므로
    # 숫자 크기에 상관없이 각 자릿수를 비교할 수 있음
    numbers.sort(key=lambda x: x*3, reverse=True)
    
    # 정렬된 순서대로 가장 큰 수를 만듦
    answer = ''
    for number in numbers:
        answer += number
    
    # 주어진 정수가 모두 0일 경우 문자열로 변환했기 때문에
    # '00'과 같은 형태로 나올 수 있으므로
    # 정수로 변환한 뒤 다시 문자열로 변환 후 반환
    return str(int(answer))