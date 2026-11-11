class Solution:
    def checkWithinK(self, arr: list[int], k: int) -> bool:
        last = {} 
        for i, x in enumerate(arr):
            if x in last and i - last[x] <= k:
                return True
            last[x] = i
        return False
