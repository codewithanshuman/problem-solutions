class Solution:
    def findPattern(self, s):
        n = len(s)
        i = 0
        while i < n:
            cx = 0
            while i < n and s[i] == 'x':
                cx += 1
                i += 1
            cy = 0
            while i < n and s[i] == 'y':
                cy += 1
                i += 1
            if cx == 0 or cx != cy:
                return False
        return True
