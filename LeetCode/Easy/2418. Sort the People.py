# 2418. Sort the People
# https://leetcode.com/problems/sort-the-people/?envType=daily-question&envId=2024-07-22

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        # 이름과 키가 각각 사람 수만큼 존재하므로
        # 계산을 위해 사람 명수를 구해줌
        N = len(names)
        
        # 이름과 키를 한번에 묶어 정렬하기 위해
        # people에 이름, 키를 묶어 삽입
        people = []
        for i in range(N):
            people.append((names[i], heights[i]))

        # lambda를 활용해 키를 기준으로 내림차순 정렬
        people.sort(key=lambda x:(x[1], x[0]), reverse=True)

        # 키를 기준으로 내림차순된 이름이 담긴 리스트가 필요하므로
        # 요구하는 반환값에 따라 만들어 반환
        ans = []
        for i in range(N):
            ans.append(people[i][0])

        return ans