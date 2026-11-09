import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    seen = {}
    out = []
    for i in range(1, n + 1):
        name = data[i]
        if name in seen:
            out.append(name + str(seen[name]))
            seen[name] += 1
        else:
            seen[name] = 1
            out.append("OK")
    sys.stdout.write("\n".join(out) + "\n")

main()
