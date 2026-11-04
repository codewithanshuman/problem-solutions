s = raw_input().strip()
t = raw_input().strip()

x1, y1 = ord(s[0]) - ord('a'), int(s[1])
x2, y2 = ord(t[0]) - ord('a'), int(t[1])

moves = []
while x1 != x2 or y1 != y2:
    m = ''
    if x1 < x2:
        m += 'R'
        x1 += 1
    elif x1 > x2:
        m += 'L'
        x1 -= 1
    if y1 < y2:
        m += 'U'
        y1 += 1
    elif y1 > y2:
        m += 'D'
        y1 -= 1
    moves.append(m)

print(len(moves))
for m in moves:
    print(m)
