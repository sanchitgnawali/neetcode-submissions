class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            # Calculate mid value
            mid = (l + r) // 2 

            # if the mid equals target, return index
            if nums[mid] == target: return mid

            # If we are in right sorted array part
            if nums[l] <= nums[mid]:
                # check if the target falls out of right sorted
                # array range
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1

            # if we are in left sorted array part
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1

        return -1
            
