# 1509. Minimum Difference Between Largest and Smallest Value in Three Moves
# https://leetcode.com/problems/minimum-difference-between-largest-and-smallest-value-in-three-moves/description/?envType=daily-question&envId=2024-07-03

class Solution:
    def minDifference(self, nums: List[int]) -> int:

        # 만약 len(nums)이 4보다 작거나 같을 경우
        # 어떤 값으로 바꿔도 0이 나오므로 0
        if len(nums) <= 4:
            return 0

        # 만약 len(nums)가 4보다 클 경우
        # 가장 큰 값과 가장 작은 값의 차이를 구해줘야 함
        else:

            # 가장 큰 값과 가장 작은 값을 구하기 위해 정렬
            nums.sort()
            ans = []

            # 둘의 차를 좁혀야 하므로 값을 바꿀 때는 3번의 기회에서
            # 항상 가장 작은 값과 가장 큰 값 중 하나를 선택해서 바꿔야 함
            # 상위3, 상위2하위1, 상위1하위2, 하위3로 4가지의 경우가 나오므로
            # 해당 경우에서 값을 바꾸고 남은 값들의 차를 계산
            for i in range(4):
                cnt = nums[len(nums)-4+i] - nums[i]
                ans.append(cnt)
            
            # 그 중 가장 작은 값을 반환
            return min(ans)