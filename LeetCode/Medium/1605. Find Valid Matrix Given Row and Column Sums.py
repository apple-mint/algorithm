# 1605. Find Valid Matrix Given Row and Column Sums
# https://leetcode.com/problems/find-valid-matrix-given-row-and-column-sums/description/?envType=daily-question&envId=2024-07-20

class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:

        # 답을 저장할 행렬 생성
        ans = [[0] * len(colSum) for _ in range(len(rowSum))]

        # 행 -> 열 순대로 탐색하면서 해당 위치에
        # 합 범위 내에서 가능한 가장 큰 수 먼저 지정
        for i in range(len(rowSum)):
            for j in range(len(colSum)):

                # 합 내여야 하므로 행합, 열합 중 작은 값으로 지정
                ans[i][j] = min(rowSum[i], colSum[j])
                
                # 지정해준 값만큼 행합, 열합을 빼줌
                rowSum[i] -= ans[i][j]
                colSum[j] -= ans[i][j]

        return ans