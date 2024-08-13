# 274. H-Index
# https://leetcode.com/problems/h-index/description/

class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """

        # h-index: 적어도 h번 인용된 논문을 적어도 h번 출판한 h의 최댓값

        # h-index가 될 수 있는 범위는
        # 0부터 한 논문이 인용된 횟수의 최댓값이므로
        # 해당값의 최댓값을 구해 maxx에 저장
        maxx = max(citations)
        
        # h-index는 최댓값을 구하는 것이므로
        # 내림차순 정렬 후 역순으로 값을 구함
        cnt = {}
        citations.sort(reverse=True)

        for i in range(len(citations)):

            # 만약 첫번째 요소라면 가장 큰 값이므로
            # 해당 논문을 인용한 횟수만큼 출판한 논문의 수는
            # 현재 값 하나이므로 1를 저장
            if not i:
                cnt[citations[i]] = 1
            
            # 그게 아니라면 해당 논문을 인용한 횟수가 그 이전값보다 작으므로
            # 해당 논문을 인용한 횟수만큼 출판한 논문의 수를
            # 현재 해당하는 논문의 수인 1과 이전값을 포함해 저장
            else:
                cnt[citations[i]] = cnt[citations[i-1]] + 1

        # 이전값을 비교하기 위한 pre 설정
        pre = 0

        # h-index가 될 수 있는 범위를 내림차순으로 탐색
        for h in range(maxx, -1, -1):

            # 만약 cnt에 해당 논문을 인용한 횟수에
            # 해당되는 출판된 논문의 수가 없다면
            # 그 이전값과 그 값이 동일하므로 해당값을 저장
            if not cnt.get(h):
                cnt[h] = pre
            
            # 만약 있다면 그 다음 탐색을 위해
            # 현재 값을 추후 비교할 값으로 갱신
            else:
                pre = cnt[h]

            # h번 인용된 논문이 적어도 h번 출판되었을 경우 해당값 반환
            if h <= cnt[h]:
                return h