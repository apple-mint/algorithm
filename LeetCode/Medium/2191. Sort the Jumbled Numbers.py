# 2191. Sort the Jumbled Numbers
# https://leetcode.com/problems/sort-the-jumbled-numbers/submissions/1331880123/?envType=daily-question&envId=2024-07-24

class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        
        # mapping 안에 있는 인덱스 번호와
        # 그 인덱스 번호의 값을 매핑해줌
        # 후에 편한 연산을 위해 문자열로 형변환해 저장
        mapp = {}
        for i in range(len(mapping)):
            mapp[str(i)] = str(mapping[i])

        new_nums = []
        for j in range(len(nums)):

            # 번호의 자릿수마다 매핑된 새로운 숫자로 바꿔줘야 하므로
            # 자릿수 탐색을 위해 문자열로 형변환
            num = str(nums[j])
            new_num = ''

            # 각 자릿수마다 새로운 숫자로 변환
            for k in range(len(num)):
                new_num += mapp[num[k]]
            
            # nums에 있던 순서를 기억하기 위해
            # 새로운 숫자와 인덱스 번호를 같이 삽입
            # 이때 오름차순으로 정렬해야 하므로
            # 새롭게 만든 숫자를 숫자로 형변환
            # 이 과정에서 '007'은 자동으로 '7'로 형변환됨
            new_nums.append((int(new_num), j))
        
        # 새롭게 만들어진 숫자를 기준으로 오름차순,
        # 그 수가 같다면 인덱스 번호를 기준으로 오름차순 정렬
        new_nums.sort()

        # 반환값에는 번호만 필요하므로
        # 인덱스 번호만 활용해 nums에 있는 번호 삽입
        ans = []
        for num, idx in new_nums:
            ans.append(nums[idx])

        return ans