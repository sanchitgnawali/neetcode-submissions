# Time O(2n)
# Space O(n)

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        temp = [0] * 2 * n

        for i in range(len(temp)):
            temp[i] = nums[i % n]

        return temp