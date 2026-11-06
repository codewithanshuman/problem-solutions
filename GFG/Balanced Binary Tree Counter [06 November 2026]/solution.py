class Solution:
    def countBT(self, h: int) -> int:
        MOD = 10**9 + 7
        if h == 1:
            return 1

        prev2, prev1 = 1, 1
        for _ in range(2, h + 1):
            cur = prev1 * ((prev1 + 2 * prev2) % MOD) % MOD
            prev2, prev1 = prev1, cur
        return prev1
