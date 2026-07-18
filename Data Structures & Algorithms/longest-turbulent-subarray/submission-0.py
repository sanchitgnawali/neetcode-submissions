# Sliding window solution
class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        res = cnt = 0
        sign = -1

        for k in range(len(arr) - 1):
            if (arr[k] > arr[k+1]):
                cnt = cnt + 1 if sign == 0 else 1
                sign = 1
            elif (arr[k] < arr[k+1]):
                cnt = cnt + 1 if sign == 1 else 1
                sign = 0
            else:
                cnt = 0
                sign = -1

            res = max(res, cnt)

        return res + 1






        