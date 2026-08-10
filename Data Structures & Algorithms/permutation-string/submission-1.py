# O(len(s1)) Time
# O(len(s1)) Space  
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        length = len(s1)
        
        for l in range(len(s2) - length + 1):
            r = l + length
            substr = s2[l:r]

            if Counter(substr) == Counter(s1):
                return True

        return False