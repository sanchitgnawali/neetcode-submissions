# This solution counts total score as we go instead of 
# doing sum() at the end
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        total = 0

        for op in operations:
            if op == "+":
                score = stack[-1] + stack[-2]
                total += score
                stack.append(score)

            elif op == "D":
                score = stack[-1] * 2
                total += score
                stack.append(score)

            elif op == "C":
                score = stack.pop()
                total -= score
            
            else:
                score = int(op)
                total += score
                stack.append(score)

        return total

            
            