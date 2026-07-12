# This solution counts total score as we go instead of 
# doing sum() at the end
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        total = 0

        for op in operations:
            if op == "+":
                total += stack[-1] + stack[-2]
                stack.append(stack[-1] + stack[-2])

            elif op == "D":
                total += stack[-1] * 2
                stack.append(stack[-1] * 2)

            elif op == "C":
                total -= stack.pop()
            
            else:
                total += int(op)
                stack.append(int(op))

        return total

            
            