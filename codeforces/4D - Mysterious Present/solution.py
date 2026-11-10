import sys
from bisect import bisect_left

def main():
    data = sys.stdin.read().split()
    n, w, h = int(data[0]), int(data[1]), int(data[2])
    env = []
    for i in range(n):
        wi = int(data[3 + 2 * i])
        hi = int(data[4 + 2 * i])
        if wi > w and hi > h:
            env.append((wi, -hi, i + 1))

    if not env:
        print(0)
        return

    env.sort() 
    m = len(env)
    prev = [-1] * m
    tails_h = []
    tails_idx = []

    for i in range(m):
        hi = -env[i][1]
        pos = bisect_left(tails_h, hi)
        if pos > 0:
            prev[i] = tails_idx[pos - 1]
        if pos == len(tails_h):
            tails_h.append(hi)
            tails_idx.append(i)
        else:
            tails_h[pos] = hi
            tails_idx[pos] = i

    print(len(tails_h))

    chain = []
    cur = tails_idx[-1]
    while cur != -1:
        chain.append(env[cur][2])
        cur = prev[cur]
    chain.reverse()
    print(" ".join(map(str, chain)))

main()
