class Solution(object):
    def busiestServers(self, k, arrival, load):
        """
        :type k: int
        :type arrival: List[int]
        :type load: List[int]
        :rtype: List[int]
        """
        free = list(range(k))
        heapq.heapify(free)
        busy = []
        count = [0] * k
        for i, (start, dur) in enumerate(zip(arrival, load)):
            while busy and busy[0][0] <= start:
                _, sid = heapq.heappop(busy)
                heapq.heappush(free, i + ((sid - i) % k))
            if not free:
                continue
            sid = heapq.heappop(free) % k
            count[sid] += 1
            heapq.heappush(busy, (start + dur, sid))
        mx = max(count)
        return [i for i, c in enumerate(count) if c == mx]
