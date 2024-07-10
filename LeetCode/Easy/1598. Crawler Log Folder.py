# 1598. Crawler Log Folder
# https://leetcode.com/problems/crawler-log-folder/description/?envType=daily-question&envId=2024-07-10

class Solution:
    def minOperations(self, logs: List[str]) -> int:

        # 하위 폴더에 얼마만큼 들어가는지를 기록
        cnt = 0

        for log in logs:

            # 상위 폴더로 올라가는 것이므로
            # 올라간 상위 폴더가 있으면 이동, 없으면 현상태 유지
            if log == "../":
                if cnt:
                    cnt -= 1

            # 현재 폴더에 머물러있으므로 현상태 유지
            elif log == "./":
                pass
            
            # 하위 폴더로 내려가는 것이므로 1을 더해줌
            else:
                cnt += 1

        return cnt