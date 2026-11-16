import sys
from math import sqrt

def dist_time_free(a, v, s, v0):

    t1 = (v - v0) / a
    d1 = (v * v - v0 * v0) / (2.0 * a)
    if d1 >= s:
        
        t = (-v0 + sqrt(v0 * v0 + 2.0 * a * s)) / a
        return t
    return t1 + (s - d1) / v

def main():
    data = sys.stdin.read().split()
    a, v, l, d, w = [float(x) for x in data[:5]]

    if w >= v:
        print("%.12f" % dist_time_free(a, v, l, 0.0))
        return
   
    dw = w * w / (2.0 * a)
    if dw >= d:
       
        print("%.12f" % dist_time_free(a, v, l, 0.0))
        return

    # => u^2 = a*d + w^2/2
    u = sqrt(a * d + w * w / 2.0)
    if u <= v:
        t = u / a + (u - w) / a
    else:
        u = v
        d_acc = v * v / (2.0 * a)
        d_brk = (v * v - w * w) / (2.0 * a)
        t = v / a + (v - w) / a + (d - d_acc - d_brk) / v
   
    t += dist_time_free(a, v, l - d, w)
    print("%.12f" % t)

main()
