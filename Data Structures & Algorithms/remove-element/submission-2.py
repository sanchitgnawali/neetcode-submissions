# Two pointers method avoiding unnecessary copying
# O(n) Time
# O(1) Space

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i, n = 0, len(nums)

        while i < n:
            if nums[i] == val:
                n -= 1
                nums[i] = nums[n]
            else:
                i += 1
        return n