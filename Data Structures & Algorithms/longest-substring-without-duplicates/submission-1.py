# Using hashmap
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        hm = {}
        count = 0

        for right in range(len(s)):
            if s[right] in hm:
                left = max(left, hm[s[right]] + 1)

            hm[s[right]] = right
            count = max(count, right - left + 1)
        
        return count