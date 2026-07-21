class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False
            
        hm = {}
        for i in range(len(s)):
            if s[i] in hm:
                hm[s[i]] += 1
            else:
                hm[s[i]] = 1
        
        for i in range(len(t)):
            if t[i] not in hm:
                return False
            elif hm[t[i]] == 0:
                return False
            else:
                hm[t[i]] -= 1

        return True


    