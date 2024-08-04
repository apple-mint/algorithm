# K번째수
# https://school.programmers.co.kr/learn/courses/30/lessons/42748

def solution(array, commands):
    answer = []
    for i, j, k in commands:
        
        # i~j번째 숫자까지 자르고 정렬 후
        # k번째에 있는 수를 구하는 것이므로
        # 인덱스 번호에 맞춰 다음과 같이 설정
        # 범위는 이상, 미만이므로 j는 별도로 연산하지 않음
        res = sorted(array[i-1:j])[k-1]

        # 주어진 조건에 따라 구한 수를 answer에 삽입
        answer.append(res)
    
    # 주어진 결과를 반환
    return answer