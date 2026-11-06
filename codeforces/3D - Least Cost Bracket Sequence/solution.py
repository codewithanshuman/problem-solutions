import sys, heapq

def main():
    data = sys.stdin.read().split()
    s = list(data[0])
    n = len(s)
    idx = 1
    heap = []
    cost = 0
    bal = 0
    for i in xrange(n):
        c = s[i]
        if c == '(':
            bal += 1
        else:
            if c == '?':
                a = int(data[idx]); b = int(data[idx + 1]); idx += 2
                s[i] = ')'
                cost += b
                heapq.heappush(heap, (a - b, i))
            bal -= 1
        if bal < 0:
            if not heap:
                print -1
                return
            d, j = heapq.heappop(heap)
            cost += d
            s[j] = '('
            bal += 2
    if bal != 0:
        print -1
        return
    print cost
    print ''.join(s)

main()
