class Solution:

    def nthCharacter(self, n):
        d, count, start = 1, 9, 1

        while n > d * count:
            n -= d * count
            d += 1
            count *= 10
            start *= 10

        num = start + (n - 1) // d
        return str(num)[(n - 1) % d]
