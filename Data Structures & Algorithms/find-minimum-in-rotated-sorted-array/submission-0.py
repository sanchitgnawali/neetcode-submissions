# O(log n) solution
class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Initialize the variables
        res = nums[0]
        l, r = 0, len(nums) - 1

        # loop till left <= right
        while l <= r:
            # Check to see if the array is sorted
            # If the array is sorted, check if leftest
            # element is minimum 
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            
            m = (l + r) // 2
            res = min(res, nums[m])
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        
        return res