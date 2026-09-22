**Notes — Largest Subsquare Surrounded by X (O(n²) solution)**

so the trick here is to stop checking "does a square of size k exist" over and over, and instead just go cell by cell, once, and ask "if this cell is the bottom-right corner of a square, how big can it get?"

**step 1: build two helper grids**

`L[i][j]` — how many X's in a row stretching left from here (including itself)
`T[i][j]` — same idea but stretching upward

super simple to build — one pass, each cell either adds 1 to its left/top neighbor's count, or resets to 1 if it's not an X or it's on the edge.

**step 2: why L and T are useful**

if you're checking a square of size k with its bottom-right corner at (i,j), you can check all 4 sides without scanning anything:

- bottom edge → `L[i][j] >= k`
- right edge → `T[i][j] >= k`
- top edge → `L[i-k+1][j] >= k`
- left edge → `T[i][j-k+1] >= k`

so border-checking becomes 4 quick lookups instead of walking along the edges.

**step 3: the part that actually makes it fast**

naive way: guess k = min(L[i][j], T[i][j]), then shrink k down one at a time until all sides pass. works, but can be slow if you're not careful.

so before shrinking, I clamp the guess using the diagonal cell:

`k = min(k, dp[i-1][j-1] + 1)`

why — a square ending at (i,j) can never be bigger than (best square ending diagonally up-left) + 1. so this makes the starting guess almost always right, meaning the while loop barely has to shrink anything in practice. this is literally the same trick from the classic "maximal square" DP problem, just adapted to check borders instead of the whole square.

**step 4: just track results**

`dp[i][j]` = best square size ending at that cell
`ans` = running max across the whole grid

**net result:** every cell touched exactly once, tiny constant-ish work per cell thanks to the diagonal cap → true O(n²), which is what actually gets past the TLE case.
