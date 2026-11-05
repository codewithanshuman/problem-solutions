import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0]); v = int(data[1])
    k = [] 
    c = []  
    for i in range(n):
        t = int(data[2 + 2 * i])
        p = int(data[3 + 2 * i])
        if t == 1:
            k.append((p, i + 1))
        else:
            c.append((p, i + 1))
    k.sort(reverse=True)
    c.sort(reverse=True)

    pk = [0]
    for p, _ in k:
        pk.append(pk[-1] + p)
    pc = [0]
    for p, _ in c:
        pc.append(pc[-1] + p)

    best = -1
    best_c = 0
    best_k = 0
    for cc in range(min(len(c), v // 2) + 1):
        kk = min(len(k), v - 2 * cc)
        total = pc[cc] + pk[kk]
        if total > best:
            best = total
            best_c = cc
            best_k = kk

    res = [idx for _, idx in c[:best_c]] + [idx for _, idx in k[:best_k]]
    sys.stdout.write(str(best) + "\n" + " ".join(map(str, res)) + "\n")

main()
