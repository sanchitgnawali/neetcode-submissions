class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total_len = len(A) + len(B)
        half = total_len // 2
        if len(A) > len(B):
            A, B = B, A

        # Find the mid so that the array is partitioned in the middle
        len_a = len(A)
        l, r = 0, len_a - 1
        while True:
            i = (l + r) // 2
            j = half - i - 2

            a_left = A[i] if i >= 0 else float("-infinity") 
            a_right = A[i + 1] if (i + 1) < len_a else float("infinity")
            b_left = B[j] if j >= 0 else float("-infinity")
            b_right = B[j + 1] if (j + 1) < len(B) else float("infinity")

            if a_left <= b_right and b_left <= a_right:
                # if odd return mininum of two left values
                if total_len % 2 == 1:
                    return min(a_right, b_right)
                return (max(a_left, b_left) + min(a_right, b_right)) / 2
            elif a_left > b_right:
                r = i - 1
            else:
                l = i + 1