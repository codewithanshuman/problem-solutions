class Solution:
    def maxPackages(self, arr: list[int], totalTime: int) -> int:
        n = len(arr)
        k = min(totalTime, n)

        window = sum(arr[:k])
        best = window

        for i in range(k, n):
            window += arr[i] - arr[i - k]
            if window > best:
                best = window

        return best
