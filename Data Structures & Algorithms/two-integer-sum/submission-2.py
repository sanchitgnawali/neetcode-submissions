class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}

        for i in range(len(nums)):
            res = target - nums[i]

            if res in hm:
                return [ hm[res], i]
            else:
                hm[nums[i]] = i

        return [-1, -1]