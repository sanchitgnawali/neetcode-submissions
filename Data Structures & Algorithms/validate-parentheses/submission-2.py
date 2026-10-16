class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hm = {
            ")" : "(", 
            "}" : "{",
            "]" : "["
        }

        for c in s:
            if c in hm:
                if not stack or stack.pop() != hm[c]:
                    return False
            else:
                stack.append(c)

        return not stack