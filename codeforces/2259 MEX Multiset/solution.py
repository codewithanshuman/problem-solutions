import sys
 
def main():
    data = sys.stdin.read().split()
    t = int(data[0]); pos = 1
    out = []
    for _ in xrange(t):
        n = int(data[pos]); pos += 1
        a = [int(x) for x in data[pos:pos + n]]; pos += n
 
        cnt = [0] * (n + 2)
        for v in a:
            if v <= n:
                cnt[v] += 1
 
        r = 0
        while cnt[r] >= 2:     
            r += 1
 
        if r == 0 and cnt[0] == 1:
            out.append("NO")
            continue
 
        out.append("YES")
        seen = [0] * (r + 1)
        res = []
        for v in a:
            if v < r:
                if seen[v] == 1:
                    res.append('C')
                else:
                    res.append('B')
                seen[v] += 1
            elif v == r and cnt[r] == 1:
                res.append('A')
            else:
                res.append('B')
        out.append("".join(res))
    sys.stdout.write("\n".join(out) + "\n")
 
main()
