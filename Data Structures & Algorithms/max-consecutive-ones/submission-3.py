# O(n) solution

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        cnt = res = 0

        for num in nums:
            if num == 1:
                cnt += 1
            else:
                res = max(cnt, res)
                cnt = 0
        
        return max(res, cnt)