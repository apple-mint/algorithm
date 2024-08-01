# 같은 숫자는 싫어
# https://school.programmers.co.kr/learn/courses/30/lessons/12906

def solution(arr):
    
    # 연속적으로 나타나는 숫자는 하나만 남겨야 하므로
    # 이전값을 비교할 변수 pre_num 생성
    answer = []
    pre_num = 0
    
    # 배열의 순서를 유지하기 위해 순차적으로 탐색
    for i in range(len(arr)):

        # 첫번째 원소라 비교할 이전값이 없으므로
        # 이전값을 비교하지 않고 바로 삽입
        if not i:
            answer.append(arr[i])
        
        # 만약 값이 이전값과 다를 경우 삽입
        else:
            if arr[i] != pre_num:
                answer.append(arr[i])
        
        # 현재 원소를 이전값으로 갱신
        pre_num = arr[i]
    
    return answer