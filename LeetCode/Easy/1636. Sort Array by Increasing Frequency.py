# 1636. Sort Array by Increasing Frequency
# https://leetcode.com/problems/sort-array-by-increasing-frequency/description/?envType=daily-question&envId=2024-07-23

# 딕셔너리에 값이 없을 경우
# 초기값을 자동적으로 설정하기 위해 사용
from collections import defaultdict

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        ans = []

        # 주어진 숫자들이 몇 번 나오는지 세줌
        dit = defaultdict(int)
        for num in nums:
            dit[num] += 1

        # 셈을 한 것을 기준으로 나온 빈도 수를 기준으로 오름차순,
        # 만약 빈도 수가 같다면 그 수를 기준으로 내림차순 정렬
        nums = sorted(dit.items(), key=lambda x: (x[1], -x[0]))

        # 순서대로 해당 값의 빈도수만큼 ans에 삽입
        for num, cnt in nums:
            for _ in range(cnt):
                ans.append(num)

        return ans