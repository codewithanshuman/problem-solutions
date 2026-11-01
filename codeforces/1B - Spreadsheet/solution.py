import re
import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    out = []
    pat = re.compile(r'^R(\d+)C(\d+)$')
    for s in data[1:n + 1]:
        m = pat.match(s)
        if m:
            row = m.group(1)
            col = int(m.group(2))
            letters = []
            while col > 0:
                col -= 1
                letters.append(chr(ord('A') + col % 26))
                col //= 26
            out.append(''.join(reversed(letters)) + row)
        else:
            i = 0
            while s[i].isalpha():
                i += 1
            col = 0
            for ch in s[:i]:
                col = col * 26 + (ord(ch) - ord('A') + 1)
            out.append('R' + s[i:] + 'C' + str(col))
    sys.stdout.write('\n'.join(out) + '\n')

main()
