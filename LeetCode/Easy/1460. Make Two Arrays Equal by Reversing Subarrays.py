# 1460. Make Two Arrays Equal by Reversing Subarrays
# https://leetcode.com/problems/make-two-arrays-equal-by-reversing-subarrays/description/?envType=daily-question&envId=2024-08-03

class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        
        # 두 배열의 길이가 같은 target, arr가 있을 때
        # arr을 arr의 일부분을 반전시켜 target과 같게 하려면
        # target과 arr의 요소가 모두 동일해야 하므로
        # 순차적 탐색을 위해 두 배열을 오름차순으로 정렬
        N = len(target)
        target.sort()
        arr.sort()
        
        # 동일한 위치에 있는 요소가 같지 않다면
        # target처럼 만들 수 없으므로 False 반환
        for i in range(N):
            if target[i] != arr[i]:
                return False

        # 만약 도중에 False 값이 반환되지 않았다면
        # 같게 만들 수 있으므로 True 반환
        return True