import sys

def main():
    data = sys.stdin.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n = int(data[pos]); pos += 1
        a = [int(x) for x in data[pos:pos + n]]
        pos += n
        m = n - 4
        v = [a[i] + a[i + 2] - a[i + 4] for i in range(m)]
        cnt = [{}, {}]          
        ans = 0
        for y in range(m):
            p = y & 1
            val = v[y]
            ans += cnt[1 - p].get(val, 0)
            same = cnt[p].get(val, 0)
            if y >= 2 and v[y - 2] == val:
                same -= 1
            if y >= 4 and v[y - 4] == val:
                same -= 1
            ans += same
            cnt[p][val] = cnt[p].get(val, 0) + 1
        out.append(str(ans))
    sys.stdout.write("\n".join(out) + "\n")

main()
