class Solution(object):
    def uniquePaths(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])
        fr = [[0] * (n + 2) for _ in range(m + 2)]
        fd = [[0] * (n + 2) for _ in range(m + 2)]
        for i in range(m - 1, -1, -1): 
            for j in range(n - 1, -1, -1):
                if grid[i][j] == 0:
                    if i == m - 1 and j == n - 1:
                        g = 1
                    else:
                        g = (fr[i][j + 1] + fd[i + 1][j]) % MOD
                    fr[i][j] = g
                    fd[i][j] = g
                else:
                    fr[i][j] = fd[i + 1][j]
                    fd[i][j] = fr[i][j + 1]
        return fr[0][0] % MOD
