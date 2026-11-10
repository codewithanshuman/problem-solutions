class Solution:
    def firstElementKTime(self, arr: list[int], k: int) -> int:
        count = {}
        for x in arr:
            c = count.get(x, 0) + 1
            if c == k:
                return x
            count[x] = c
        return -1
