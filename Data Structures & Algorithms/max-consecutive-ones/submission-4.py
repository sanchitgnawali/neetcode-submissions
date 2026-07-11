# shortest o(n) solution

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = maxOnes = 0

        for num in nums:
            count = count + 1 if num else 0
            maxOnes = max(count, maxOnes)

        return maxOnes