Every palindrome has a middle, so I try every possible middle and spread outward while both sides match.

There are two kinds of middle. In "aba" it's the letter b, so I start at (i, i). In "abba" it's the gap between the b's, so I start at (i, i+1).

The loop is simple - while l and r are in range and s[l] == s[r], move l left and r right. It overshoots by one on each side, so the answer is s[l+1 : r]. I keep the longest one.

Time is O(n²), space is O(1). Fine for n ≤ 1000.

Mistakes I made:

typed the function name differently in the def and the call
wrote s[1] instead of s[l]
forgot the even case, so "cbbd" failed

Happy Coding :)
