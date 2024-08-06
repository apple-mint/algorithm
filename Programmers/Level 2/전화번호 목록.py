# 전화번호 목록
# https://school.programmers.co.kr/learn/courses/30/lessons/42577

def solution(phone_book):

    # 한 번호가 다른 번호의 접두사가 되므로
    # 탐색을 위해 접두사가 될 번호의 길이 측정
    # 길이가 같은 번호가 있을 수 있으므로
    # 중복을 제거할 수 있는 set에 계산값을 저장
    phone_len = set()
    for phone in phone_book:
        phone_len.add(len(phone))

    # 길이가 짧은 번호부터 순차적으로
    # 탐색할 수 있도록 오름차순 정렬
    phone_len = sorted(phone_len)
    
    # 어떤 번호가 다른 번호의 접두어인지 확인
    answer = True
    
    # 접두사를 담을 딕셔너리
    prefix = {}

    # 길이가 짧은 번호부터 순차적으로 탐색할 수 있도록
    # 길이를 기준으로 오름차순 정렬
    # phone_book에 담긴 요소들은 문자열이므로
    # 만약 길이가 같을 경우 각 자릿수에서 숫자가 작은 순으로 정렬됨
    phone_book.sort(key=lambda x:len(x))

    # 탐색 시작
    for phone in phone_book:

        for n in phone_len:

            # 만약 n이 현재 번호의 길이보다 길다면
            # 접두사가 될 수 없으므로 break
            if len(phone) < n:
                break
            
            # 주어진 n의 길이만큼 잘라 접두사를 만들고
            # 그 접두사가 다른 전체 번호인지 확인
            pre = phone[0:n]

            # 만약 그 값이 있다면 어떤 번호가
            # 해당 번호의 접두사이므로 값 변경 후 break
            if prefix.get(pre):
                answer = False
                break
            
            # 만약 그렇지 않다면 해당 번호의 길이가
            # n과 같다면 새로운 접두사로 prefix에 추가
            if len(phone) == n:
                prefix[pre] = 1
    
    return answer