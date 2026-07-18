class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = right = 0
        n = len(nums)

        while right < n:
            nums[left] = nums[right]

            while right < n and nums[right] == nums[left]:
                right += 1
            left += 1
        return left

