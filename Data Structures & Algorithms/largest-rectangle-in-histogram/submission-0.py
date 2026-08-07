class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # initialize maxArea and Stack
        maxArea = 0
        stack = []

        # Loop through heights
        for i, h in enumerate(heights):
            start = i
            # if the height at current index is smaller than
            # height in the top of the stack, pop it and calculate
            # the area
            # To extend the current height backwards keep start as
            # the index of the popped height
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))
                start = index
        
            stack.append((start, h))
        
        # Loop through each element in the stack
        for index, height in stack:
            maxArea = max(maxArea, height * (len(heights) - index))

        
        return maxArea
    