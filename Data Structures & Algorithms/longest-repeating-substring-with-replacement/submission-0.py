class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hm = {}
        left = 0
        res = 0
        maximum = 0

        for right in range(len(s)):
            hm[s[right]] = 1 + hm.get(s[right], 0)
            
            if (right - left + 1) - max(hm.values()) > k:
                hm[s[left]] -= 1
                left += 1
            
            res = max(res, right - left + 1)

        return res
            
                

            