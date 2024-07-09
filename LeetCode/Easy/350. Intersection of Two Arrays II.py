# 350. Intersection of Two Arrays II
# https://leetcode.com/problems/intersection-of-two-arrays-ii/description/?envType=daily-question&envId=2024-07-02

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []

        dit1 = {}
        dit2 = {}

        # nums1, nums2에는 0~1000까지 숫자가 있으므로
        # 이 숫자가 있는지 확인하기 위해 dit1, dit2 설정
        for num in range(0, 1001):
            dit1[num] = 0
            dit2[num] = 0

        # 숫자가 있는지 확인
        for num1 in nums1:
            dit1[num1] += 1
        
        for num2 in nums2:
            dit2[num2] += 1

        # nums1에 있는 수가 nums2에 있는지 확인하기 위해 중복 제거
        check = set(nums1)

        for num1 in check:

            # 만약 있다면 그 수만큼 ans에 추가
            if num1 in nums2:
                if dit1[num1] <= dit2[num1]:
                    cnt = dit1[num1]
                    for _ in range(cnt):
                        ans.append(num1)
                else:
                    cnt = dit2[num1]
                    for _ in range(cnt):
                        ans.append(num1)

        return ans