class Solution(object):
    def minOperations(self, nums, x, k):
        """
        :type nums: List[int]
        :type x: int
        :type k: int
        :rtype: int
        """
        n = len(nums)
        m = n - x + 1
        cost = [0] * m
        lo = []
        hi = []
        side = [0] * n
        dead = [False] * n
        st = [0, 0, 0 ,0]
        def prune_lo():
            while lo and dead[lo[0][1]]:
                heapq.heappop(lo)
        def prune_hi():
            while hi and dead[hi[0][1]]:
                heapq.heappop(hi)
        def rebalance():
            if st[0] > st[1] + 1:
                prune_lo()
                nv, j = heapq.heappop(lo)
                v = -nv
                heapq.heappush(hi, (v, j))
                side[j] = 1
                st[0] -= 1; st[1] += 1
                st[2] -= v; st[3] += v
            elif st[0] < st[1]:
                prune_hi()
                v, j = heapq.heappop(hi)
                heapq.heappush(lo, (-v, j))
                side[j] = 0
                st[1] -= 1; st[0] += 1
                st[3] -= v; st[2] += v

        def add(i):
            v = nums[i]
            prune_lo()
            if not lo or v <= -lo[0][0]:
                heapq.heappush(lo, (-v,i))
                side[i] = 0
                st[0] += 1; st[2] += v
            else:
                heapq.heappush(hi, (v, i))
                side[i] = 1
                st[1] += 1; st[3] += v
            rebalance()
        def remove(i):
            v = nums[i]
            dead[i] = True
            if side[i] == 0:
                st[0] -= 1; st[2] -= v

            else:
                st[1] -= 1; st[3] -= v
            prune_lo()
            prune_hi()
            rebalance()
        for i in range(n):
            add(i)
            if i >= x:
                remove(i - x)
            if i >= x - 1:
                prune_lo()
                med = -lo[0][0]
                cost[i - x + 1] = (med * st[0] - st[2]) + (st[3] - med * st[1])
        INF = float('inf')
        prev = [0] * (n + 1)
        for j in range(1, k + 1):
            cur = [INF] * (n + 1)
            for i in range(1, n + 1):
                best = cur[i - 1]
                if i >= x and prev[i - x] != INF:
                    c = prev[i - x] + cost[i - x]
                    if c < best:
                        best = c
                cur[i] = best
            prev = cur
        return prev[n]
