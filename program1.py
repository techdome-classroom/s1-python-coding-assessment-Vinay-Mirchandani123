class Solution:
   
    def getTotalIsles(self, grid: list[list[str]]) -> int:
    #    write your code here
        if not grid:
            return 0
            def dfs(grid, i, j):
                if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 'W':
                    return
                grid[i][j] = 'W'  # Mark the landmass as visited
                dfs(grid, i + 1, j)  # Check down
                dfs(grid, i - 1, j)  # Check up
                dfs(grid, i, j + 1)  # Check right
                dfs(grid, i, j - 1)  # Check left

        island_count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 'L':
                    dfs(grid, i, j)
                    island_count += 1

        return island_count
                    
