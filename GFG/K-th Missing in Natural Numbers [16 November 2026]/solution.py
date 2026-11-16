class Solution:
    def findKthSmall(self, arr, k):
        lo, hi = 1, k + len(arr)  
        while lo < hi:
            mid = (lo + hi) // 2
            removed = 0
            for v in arr:
                if v <= mid:
                    removed += 1
            if mid - removed >= k:
                hi = mid
            else:
                lo = mid + 1
        return lo
