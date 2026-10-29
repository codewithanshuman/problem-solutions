class Solution(object):
    def palindromePath(self, n, edges, s, queries):
        """
        :type n: int
        :type edges: List[List[int]]
        :type s: str
        :type queries: List[str]
        :rtype: List[bool]
        """
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        LOG = max(1, n.bit_length())
        up = [[0] * n for _ in range(LOG)]
        depth = [0] * n
        tin = [0] * n
        size = [1] * n
        order = []
        stack = [0]
        visited = [False] * n
        visited[0] = True
        while stack:
            u = stack.pop()
            tin[u] = len(order)
            order.append(u)
            for w in adj[u]:
                if not visited[w]:
                    visited[w] = True
                    up[0][w] = u
                    depth[w] = depth[u] + 1
                    stack.append(w)
        for u in reversed(order):
            if u != 0:
                size[up[0][u]] += size[u]
        for k in range(1, LOG):
            prev, cur = up[k - 1], up[k]
            for v in range(n):
                cur[v] = prev[prev[v]]
        def lca(a, b):
            if depth[a] < depth[b]:
                a, b = b, a
            diff = depth[a] - depth[b]
            k = 0
            while diff:
                if diff & 1:
                    a = up[k][a]
                diff >>= 1
                k += 1
            if a == b:
                return a
            for k in range(LOG - 1, -1, -1):
                if up[k][a] != up[k][b]:
                    a = up[k][a]
                    b = up[k][b]
            return up[0][a]
        bit = [0] * (n + 2)
        def upd(i, m):
            i += 1
            while i <= n + 1:
                bit[i] ^= m
                i += i & -i
        def pref(i):
            i += 1
            r = 0
            while i > 0:
                r ^= bit[i]
                i -= i & -i
            return r
        def range_xor(u, m):
            upd(tin[u], m)
            upd(tin[u] + size[u], m)
        chars = [ord(ch) - 97 for ch in s]
        for u in range(n):
            range_xor(u, 1 << chars[u])
        ans = []
        for q in queries:
            parts = q.split()
            if parts[0] == "update":
                u = int(parts[1])
                c = ord(parts[2]) - 97
                if c != chars[u]:
                    range_xor(u, (1 << chars[u]) ^ (1 << c))
                    chars[u] = c
            else:
                u, v = int(parts[1]), int(parts[2])
                l = lca(u, v)
                mask = pref(tin[u]) ^ pref(tin[v]) ^ (1 << chars[l])
                ans.append(mask & (mask - 1) == 0)

        return ans
