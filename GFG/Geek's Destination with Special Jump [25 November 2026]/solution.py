class Solution:
    def minTime(self, a: int, b: int, d: int, l: int, r: int) -> int:
        MOD = 10**9 + 7
        c = a - b

        def G(x):
            if x <= a:
                return 0
            M = x - a
            q, rem = divmod(M, c)
            return c * q * (q + 1) // 2 + rem * (q + 1)

        lo, hi = d - r, d - l          
        cnt = hi - lo + 1
        sum_p1 = (lo + hi) * cnt // 2 + cnt  
        ksum = G(hi) - G(lo - 1)
        return (sum_p1 + 2 * b * ksum) % MOD
