from typing import List

class Solution:

    def cntSubsets(self, arr: List[int], l: int, r: int) -> int:
        MOD = 10**9 + 7
        n = len(arr)

        cnt = [0] * (n + 2)
        for x in arr:
            cnt[x] += 1

        pow2 = [1] * (n + 1)
        for i in range(1, n + 1):
            pow2[i] = pow2[i - 1] * 2 % MOD

        ans = 0
        prod = 1    
        seen = 0     
        for m in range(0, r + 1):
            seen += cnt[m]
            if m >= l:
                greater = n - seen            
                ans = (ans + prod * pow2[greater]) % MOD

            prod = prod * (pow2[cnt[m]] - 1) % MOD
            if prod == 0:
                break

        return ans
