class Solution:
    def largestSumCycle(self, edge):
        n = len(edge)
        state = [0] * n   
        best = -1

        for start in range(n):
            if state[start] != 0:
                continue

            path = []
            cur = start
            while cur != -1 and state[cur] == 0:
                state[cur] = 1
                path.append(cur)
                cur = edge[cur]

            if cur != -1 and state[cur] == 1:
                total = 0
                j = len(path) - 1
                while True:
                    total += path[j]
                    if path[j] == cur:
                        break
                    j -= 1
                best = max(best, total)

            for node in path:
                state[node] = 2

        return best
