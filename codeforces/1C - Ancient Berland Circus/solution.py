import sys
from math import *

def main():
    data = sys.stdin.read().split()
    p = [(float(data[2*i]), float(data[2*i+1])) for i in range(3)]

    def dist(u, v):
        return hypot(u[0]-v[0], u[1]-v[1])

    a = dist(p[1], p[2])
    b = dist(p[0], p[2])
    c = dist(p[0], p[1])

    s = (a + b + c) / 2.0
    area = sqrt(max(s*(s-a)*(s-b)*(s-c), 0.0))
    R = a * b * c / (4.0 * area)

    
    def ang(x, y, z):
        v = (y*y + z*z - x*x) / (2.0*y*z)
        return acos(max(-1.0, min(1.0, v)))

    A = ang(a, b, c)
    B = ang(b, a, c)
    C = pi - A - B

    def is_int(v):
        return abs(v - round(v)) < 1e-4

    for n in range(3, 101):
        if is_int(A * n / pi) and is_int(B * n / pi) and is_int(C * n / pi):
            print("%.8f" % (n / 2.0 * R * R * sin(2 * pi / n)))
            return

main()
