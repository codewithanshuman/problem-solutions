class Solution:
    def maximumWeight(self, n, edges, queries):
        parent = list(range(n + 1))
        size = [1] * (n + 1)

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]] 
                x = parent[x]
            return x


        edges_sorted = sorted(edges, key=lambda e: e[2])


        order = sorted(range(len(queries)), key=lambda i: queries[i])

        res = [0] * len(queries)
        total = 0
        j = 0
        m = len(edges_sorted)

        for qi in order:
            x = queries[qi]
   
            while j < m and edges_sorted[j][2] <= x:
                u, v, _ = edges_sorted[j]
                ru, rv = find(u), find(v)
                if ru != rv:
                    total += size[ru] * size[rv]
  
                    if size[ru] < size[rv]:
                        ru, rv = rv, ru
                    parent[rv] = ru
                    size[ru] += size[rv]
                j += 1
            res[qi] = total

        return res
