# 1380. Lucky Numbers in a Matrix
# https://leetcode.com/problems/lucky-numbers-in-a-matrix/description/?envType=daily-question&envId=2024-07-19

class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:

        # M: matrix 열, N: martix 행
        # 열은 세로줄이므로 []가 총 몇 개인지를 확인하고
        # 행은 가로줄이므로 하나의 []에 총 몇 개가 있는지를 확인
        M = len(matrix)
        N = len(matrix[0])

        # 각 행에서 최솟값이 무엇인지 구하기 위해 행 탐색 후
        # 찾은 최솟값을 하나의 행 탐색 종료 후 mini에 삽입
        mini = []
        for i in range(M):
            minn = float('inf')
            for j in range(N):
                if matrix[i][j] < minn:
                    minn = matrix[i][j]

            mini.append(minn)

        # 각 열에서 최댓값이 무엇인지 구하기 위해 열 탐색 후
        # 찾은 최댓값을 하나의 열 탐색 종료 후 maxi에 삽입
        maxi = []
        for i in range(N):
            maxx = float('-inf')
            for j in range(M):
                if matrix[j][i] > maxx:
                    maxx = matrix[j][i]
            
            maxi.append(maxx)

        # 행에서 최솟값이자 열에서 최댓값인 값인
        # lucky number를 찾기 위해 matrix 전체를 탐색
        ans = []
        for i in range(M):
            for j in range(N):

                # mini, maxi의 인덱스는 각 행, 열 인덱스이므로
                # 최솟값, 최댓값을 찾을 때 별도의 인덱스를 기록할 필요 없음
                # 만약 해당 값이 조건을 만족한다면 ans에 삽입
                if matrix[i][j] == mini[i] == maxi[j]:
                    ans.append(matrix[i][j])

        return ans