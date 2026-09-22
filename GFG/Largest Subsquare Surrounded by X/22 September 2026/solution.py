class Solution:
    def largestSubsquare(self, mat):
        n = len(mat)
        L = [[0]*n for _ in range(n)]
        T = [[0]*n for _ in range(n)]
        
        for i in range(n):
            for j in range(n):
                if mat[i][j] == 'X':
                    L[i][j] = L[i][j-1] + 1 if j > 0 else 1
                    T[i][j] = T[i-1][j] + 1 if i > 0 else 1



      
        dp = [[0]*n for _ in range(n)]
        ans = 0
        
        for i in range(n):
            for j in range(n):
                if mat[i][j] != 'X':
                    continue
                k = min(L[i][j], T[i][j])
                if i > 0 and j > 0:
                    k = min(k, dp[i-1][j-1] + 1)

                while k > 1 and not (L[i-k+1][j] >= k and T[i][j-k+1] >= k):
                    k -= 1
                
                dp[i][j] = k
                ans = max(ans, k)



      
        return ans
