d, s = map(int, raw_input().split())
lo = []
hi = []
for _ in range(d):
    a, b = map(int, raw_input().split())
    lo.append(a)
    hi.append(b)

if s < sum(lo) or s > sum(hi):
    print "NO"
else:
    rem = s - sum(lo)
    res = lo[:]
    for i in range(d):
        add = min(rem, hi[i] - lo[i])
        res[i] += add
        rem -= add
    print "YES"
    print " ".join(map(str, res))
