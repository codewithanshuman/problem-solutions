class Solution:
    def sortIt(self, arr):
        odds = sorted((x for x in arr if x & 1), reverse=True)
        evens = sorted(x for x in arr if not x & 1)
        arr[:] = odds + evens
