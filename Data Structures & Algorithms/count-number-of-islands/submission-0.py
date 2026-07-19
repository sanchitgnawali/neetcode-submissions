class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[1,0], [-1,0], [0, 1], [0, -1]]
        rows, cols = len(grid), len(grid[0])
        islands = 0

        def bfs(r, c):
            q = deque()
            grid[r][c] = "0"
            q.append((r,c))

            while q:
                row, col = q.popleft()

                for x,y in directions:
                    dx, dy = row + x, col + y

                    if (dx < 0 or dy < 0
                        or dx >= rows or dy >= cols 
                        or grid[dx][dy] == "0"):
                            continue

                    q.append((dx, dy))
                    grid[dx][dy] = "0"

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    bfs(r,c)
                    islands += 1

        return islands