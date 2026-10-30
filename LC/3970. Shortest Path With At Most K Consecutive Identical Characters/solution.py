class Solution(object):
    def shortestPath(self, n, edges, labels, k):
        """
        :type n: int
        :type edges: List[List[int]]
        :type labels: str
        :type k: int
        :rtype: int
        """
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))
        INF = float('inf')
        stride = k + 1
        dist = [INF] * (n * stride)
        dist[1] = 0
        pq = [(0, 0, 1)]
        while pq:
            d, u, r = heapq.heappop(pq)
            if d > dist[u * stride + r]:
                continue
            if u == n - 1:
                return d
            lu = labels[u]
            for v, w in adj[u]:
                if labels[v] == lu:
                    nr = r + 1
                    if nr > k:
                        continue
                else:
                    nr = 1
                nd = d + w
                idx = v * stride + nr
                if nd < dist[idx]:
                    dist[idx] = nd
                    heapq,heappush(pq, (nd, v, nr))

        return -1
