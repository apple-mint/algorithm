# 폰켓몬
# https://school.programmers.co.kr/learn/courses/30/lessons/1845

def solution(nums):
    
    # 같은 종류의 폰켓몬의 수를 세줌
    phonekemon = {}
    for num in nums:
        if not phonekemon.get(num):
            phonekemon[num] = 1
        else:
            phonekemon[num] += 1

    # N: 폰켓몬의 수
    N = len(nums)
    
    # 만약 폰켓몬 종류의 수가 뽑을 수 있는 폰켓몬의 수인 N//2와
    # 같거나 작을 경우 모든 폰켓몬 종류를 고를 수 있으므로
    # 폰켓몬 종류의 수를 반환
    if len(phonekemon) <= N//2:
        answer = len(phonekemon)

    # 아니라면 폰켓몬을 고를 수 있는 만큼이 최대이므로
    # 뽑을 수 있는 폰켓몬의 수인 N//2를 반환
    else:
        answer = N//2
    
    return answer