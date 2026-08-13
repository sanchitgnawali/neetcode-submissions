class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""
        
        window = {}
        count_t = {}
        
        # get the count of t
        for c in t:
            count_t[c] = 1 + count_t.get(c, 0)

        # Use two pointers
        l = 0
        need, have = len(count_t), 0
        max_len = float("inf")
        res = [-1, -1]
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in count_t and window[c] == count_t[c]:
                have += 1

            while have == need:
                if (r - l + 1) <  max_len:
                    max_len = r - l + 1
                    res = [l, r]
                
                window[s[l]] -= 1

                if s[l] in count_t and window[s[l]] < count_t[s[l]]:
                    have -= 1
                
                l += 1
        
        l, r= res
        return s[l:r+1] if max_len != float("inf") else ""