class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
            
        pointer = 0
        sum = 0
        res = nums[0]

        while pointer < len(nums):
            sum = max(0, sum)
            sum += nums[pointer]
            res = max(res, sum)

            pointer += 1

        return res
        
