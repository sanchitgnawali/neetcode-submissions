class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        rows, cols = len(grid), len(grid[0])
        maxCount = 0

        def bfs(r,c) -> int:
            q = deque()
            q.append((r,c))
            size = 1
            grid[r][c] = 0

            while q:
                row, col = q.popleft()

                for dx, dy in directions:
                    new_row = row + dx
                    new_col = col + dy

                    if (new_row < 0 or new_col < 0 
                        or new_row >= rows or new_col >= cols
                        or grid[new_row][new_col] == 0):
                            continue
                    
                    size += 1
                    q.append((new_row, new_col))
                    grid[new_row][new_col] = 0

            return size


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    size = bfs(r,c)
                    maxCount = max(maxCount, size)
        
        return maxCount