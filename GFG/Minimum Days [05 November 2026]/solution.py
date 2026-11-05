class Solution:
    def getMinimumDays(self, s: str, p: list[int]) -> int:
        n = len(s)

        day_of = [0] * n
        for i, idx in enumerate(p):
            day_of[idx] = i + 1

        def ok(days):

            for i in range(n - 1):
                if s[i] == s[i + 1] and day_of[i] > days and day_of[i + 1] > days:
                    return False
            return True

        lo, hi = 0, n
        while lo < hi:
            mid = (lo + hi) // 2
            if ok(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo
