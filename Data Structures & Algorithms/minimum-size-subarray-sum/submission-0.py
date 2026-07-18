class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        currentSum = 0
        minCount = float('inf')
        
        for right in range(len(nums)):
            currentSum += nums[right]

            while currentSum >= target:
                minCount = min(minCount, right - left + 1)
                currentSum -= nums[left]
                left+= 1

        return 0 if minCount == float('inf') else minCount
    