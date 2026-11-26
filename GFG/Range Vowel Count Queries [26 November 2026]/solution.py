class Solution:
    def countVowels(self, s: str, queries: list[list[int]]) -> list[int]:
        vowels = set("aeiou")
        n = len(s)

        prefix = [0] * (n + 1)
        for i, ch in enumerate(s):
            prefix[i + 1] = prefix[i] + (ch in vowels)

        return [prefix[r + 1] - prefix[l] for l, r in queries]
