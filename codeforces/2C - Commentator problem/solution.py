import sys, math

def main():
    data = sys.stdin.read().replace(',', ' ').split()
    v = [float(t) for t in data[:9]]
    x1, y1, r1, x2, y2, r2, x3, y3, r3 = v

    def eq(xa, ya, ra, xb, yb, rb):
        A = rb*rb - ra*ra
        B = -2*rb*rb*xa + 2*ra*ra*xb
        C = -2*rb*rb*ya + 2*ra*ra*yb
        D = rb*rb*(xa*xa + ya*ya) - ra*ra*(xb*xb + yb*yb)
        return A, B, C, D

    A1, B1, C1, D1 = eq(x1, y1, r1, x2, y2, r2)
    A2, B2, C2, D2 = eq(x1, y1, r1, x3, y3, r3)

    pts = []
    if A1 == 0 and A2 == 0:
        det = B1 * C2 - B2 * C1
        if det != 0:
            x = (-D1 * C2 + D2 * C1) / det
            y = (-B1 * D2 + B2 * D1) / det
            pts.append((x, y))
    else:
        if A1 == 0:
            la, lb, lc = B1, C1, D1
            A, B, C, D = A2, B2, C2, D2
        elif A2 == 0:
            la, lb, lc = B2, C2, D2
            A, B, C, D = A1, B1, C1, D1
        else:
            la = A2 * B1 - A1 * B2
            lb = A2 * C1 - A1 * C2
            lc = A2 * D1 - A1 * D2
            A, B, C, D = A1, B1, C1, D1
        p, q, s = B / A, C / A, D / A
        cx, cy = -p / 2.0, -q / 2.0
        R2 = cx * cx + cy * cy - s
        n2 = la * la + lb * lb
        if n2 > 0:
            t = (la * cx + lb * cy + lc) / n2
            fx, fy = cx - la * t, cy - lb * t
            dist2 = t * t * n2
            h2 = R2 - dist2
            eps = 1e-9 * max(1.0, abs(R2))
            if h2 >= -eps:
                h = math.sqrt(max(h2, 0.0))
                n = math.sqrt(n2)
                dx, dy = -lb / n, la / n
                pts.append((fx + dx * h, fy + dy * h))
                if h > 0:
                    pts.append((fx - dx * h, fy - dy * h))

    if not pts:
        return
    best = min(pts, key=lambda P: (P[0] - x1) ** 2 + (P[1] - y1) ** 2)
    print("%.5f %.5f" % (best[0], best[1]))

main()
