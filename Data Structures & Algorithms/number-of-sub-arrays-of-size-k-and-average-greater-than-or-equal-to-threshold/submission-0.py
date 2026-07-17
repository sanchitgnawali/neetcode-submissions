# Sliding window solution
class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        L = 0
        currSum = 0
        result = 0

        for R in range(len(arr)):
            
            if R - L >= k:
                currSum -= arr[L]
                L += 1
            
            currSum += arr[R]
            
            if (R - L) == (k-1) and currSum / k >= threshold:
                result += 1
        
        return result
            


