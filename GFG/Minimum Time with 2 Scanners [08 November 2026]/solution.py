class Solution:
    def minTime(self, n: int, s1: int, s2: int) -> int:
        lo, hi = 1, min(s1, s2) * n
        while lo < hi:
            mid = (lo + hi) // 2
            if mid // s1 + mid // s2 >= n:
                hi = mid
            else:
                lo = mid + 1
        return lo
