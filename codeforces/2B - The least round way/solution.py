import sys

def main():
    rl = sys.stdin.readline
    n = int(rl())
    D2 = []  
    D5 = []
    p2 = p5 = None
    zero = None
    for i in xrange(n):
        row = map(int, rl().split())
        A = [0] * n
        B = [0] * n
        for j in xrange(n):
            v = row[j]
            if v == 0:
                if zero is None:
                    zero = (i, j)
                A[j] = 1
                B[j] = 1
            else:
                A[j] = (v & -v).bit_length() - 1
                if v % 5 == 0:
                    b = 0
                    while v % 5 == 0:
                        v //= 5
                        b += 1
                    B[j] = b
        c2 = [0] * n
        c5 = [0] * n
        r2 = bytearray(n)
        r5 = bytearray(n)
        if i == 0:
            l2 = l5 = 0
            for j in xrange(n):
                l2 += A[j]
                l5 += B[j]
                c2[j] = l2
                c5[j] = l5
        else:
            l2 = p2[0] + A[0]
            l5 = p5[0] + B[0]
            c2[0] = l2
            c5[0] = l5
            r2[0] = 1
            r5[0] = 1
            for j in xrange(1, n):
                u = p2[j]
                if u < l2:
                    l2 = u + A[j]
                    r2[j] = 1
                else:
                    l2 += A[j]
                c2[j] = l2
                u = p5[j]
                if u < l5:
                    l5 = u + B[j]
                    r5[j] = 1
                else:
                    l5 += B[j]
                c5[j] = l5
        D2.append(r2)
        D5.append(r5)
        p2, p5 = c2, c5

    t2 = p2[n - 1]
    t5 = p5[n - 1]
    res = min(t2, t5)
    if zero is not None and res > 1:
        zi, zj = zero
        print 1
        print 'D' * zi + 'R' * zj + 'D' * (n - 1 - zi) + 'R' * (n - 1 - zj)
        return

    D = D2 if t2 <= t5 else D5
    path = []
    i = j = n - 1
    while i or j:
        if i and (j == 0 or D[i][j]):
            path.append('D')
            i -= 1
        else:
            path.append('R')
            j -= 1
    path.reverse()
    print res
    print ''.join(path)

main()
