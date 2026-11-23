class Solution:
    def posInfinite(self, s: str, pos: int) -> str:

        lengths = [len(s)]
        i = 0
        while lengths[-1] < pos:
            i += 1
            lengths.append(2 * lengths[-1] + i)

        p = pos

        for lvl in range(len(lengths) - 1, 0, -1):
            L = lengths[lvl - 1]
            if p <= L:
                continue
            if p <= L + lvl:
                return '$'
            q = p - L - lvl        
            p = L - q + 1            

        return s[p - 1]
