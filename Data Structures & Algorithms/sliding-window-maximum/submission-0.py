# Sliding Window
# Time: O(n) Space: O(n)
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = r = 0
        output = []
        q = collections.deque()
        # Loop through each element in the array
        while r < len(nums):
            # while nums[r] is greater than last element in the queue
            # pop the last element in the queue
            while q and q[-1] < nums[r]:
                q.pop()

            q.append(nums[r])

            # if r + 1 (1 is added to r because r is 0-indexed) is 
            # greater than or equal to k, we meet the criteria for 
            # the window
            if r + 1 >= k:
                output.append(q[0])

                # popleft on q when left element in the queue
                # goes out of the window
                if nums[l] == q[0]:
                    q.popleft()
                
                l += 1
            
            r += 1

        return output
