import sys

def main():
    g = [sys.stdin.readline().strip() for _ in range(3)]
    flat = "".join(g)
    x = flat.count('X')
    o = flat.count('0')

    lines = []
    for i in range(3):
        lines.append([(i, 0), (i, 1), (i, 2)])
        lines.append([(0, i), (1, i), (2, i)])
    lines.append([(0, 0), (1, 1), (2, 2)])
    lines.append([(0, 2), (1, 1), (2, 0)])

    def wins(ch):
        for ln in lines:
            if all(g[r][c] == ch for r, c in ln):
                return True
        return False

    xw = wins('X')
    ow = wins('0')


    if not (x == o or x == o + 1):
        print("illegal")
        return
    if xw and ow:
        print("illegal")
        return
    if xw:

        print("the first player won" if x == o + 1 else "illegal")
        return
    if ow:

        print("the second player won" if x == o else "illegal")
        return
    if x + o == 9:
        print("draw")
        return
    print("first" if x == o else "second")

main()
