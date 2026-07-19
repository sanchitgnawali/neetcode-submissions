class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        originalColor = image[sr][sc]

        if originalColor == color:
            return image

        def changeColor(i,j):
            if i < 0 or i > (len(image)-1):
                return
            if j < 0 or j > (len(image[0]) - 1):
                return

            if image[i][j] != originalColor: 
                return

            
            image[i][j] = color
            
            changeColor(i, j+1)
            changeColor(i+1, j)
            changeColor(i, j-1)
            changeColor(i-1, j)

        changeColor(sr, sc)
        return image