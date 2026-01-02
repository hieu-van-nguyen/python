from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ROWS, COLS = len(grid), len(grid[0])
        count = 0
        visited = [[False for _ in range(COLS)] for _ in range(ROWS)]

        def dfs(r, c):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or visited[r][c]:
                return
            visited[r][c] = True
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        for r in range(ROWS):
            for c in range(COLS):
                    count += 1
                    dfs(r, c)
        
        return count