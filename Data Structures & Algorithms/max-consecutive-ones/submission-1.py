# O(n^2) solution
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        for i in range(0,len(nums)):
            cnt = 0
            for j in range(i,len(nums)):
                if nums[j] == 0: break
                cnt += 1
            res = max(res, cnt)
        
        return res