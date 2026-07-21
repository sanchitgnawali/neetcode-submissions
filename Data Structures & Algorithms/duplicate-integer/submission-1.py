# Using hashset
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # if the length of set is smaller than original length
        # the array contains duplicate values
        return len(set(nums)) < len(nums)
        