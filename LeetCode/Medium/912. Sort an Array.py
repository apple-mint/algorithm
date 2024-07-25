# 912. Sort an Array
# https://leetcode.com/problems/sort-an-array/description/?envType=daily-question&envId=2024-07-25

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        # 오름차순이므로 sort를 사용하면 되나
        # 내장함수를 쓰지 말라고 명시되어 있으므로 딕셔너리를 활용
        dit = {}

        # 주어진 num의 범위만큼 딕셔너리 초기값 설정
        for n in range(-5*10**4, 5*10**4+1):
            dit[n] = 0

        # 해당되는 값이 나오는 수만큼 value 값 갱신
        for num in nums:
            dit[num] += 1

        ans = []

        # 딕셔너리를 num이 될 수 있는 오름차순으로 설정했으므로
        # key, value를 순차적으로 탐색하며
        # 해당되는 값이 나온 수만큼 ans에 삽입
        for num, cnt in dit.items():
            for _ in range(cnt):
                ans.append(num)

        return ans