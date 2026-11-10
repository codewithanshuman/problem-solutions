class Solution(object):
    def climbStairs(self, n, costs):
        """
        :type n: int
        :type costs: List[int]
        :rtype: int
        """
        INF = float('inf')
        dp = [INF] * (n + 1)
        dp[0]= 0
        for j in range(1, n + 1):
            c = costs[j - 1]
            for k in (1, 2, 3):
                i = j - k
                if j >= 0:
                    cand = dp[i] + c + k * k
                    if cand < dp[j]:
                        dp[j] = cand
        return dp[n]
