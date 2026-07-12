# Bruteforce approach
# O(n) runtime
# O(n) Space
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        temp = []

        for i in range(len(nums)):
            if nums[i] == val:
                continue
            temp.append(nums[i])
        
        for i in range(len(temp)):
            nums[i] = temp[i]
        
        return len(temp)
                    
                