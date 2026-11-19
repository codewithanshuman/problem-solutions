class Solution:
    def findXOR(self, l: int, r: int) -> int:
        def prefix(n):
            m = n % 4
            if m == 0:
                return n
            if m == 1:
                return 1
            if m == 2:
                return n + 1
            return 0

        return prefix(r) ^ prefix(l - 1)
