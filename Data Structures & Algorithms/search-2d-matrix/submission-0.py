class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for list in matrix:
            for num in list:
                if num == target:
                    return True
        
        return False