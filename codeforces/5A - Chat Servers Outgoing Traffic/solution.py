import sys

count = 0
total = 0
for line in sys.stdin:
    line = line.rstrip('\r\n')
    if not line:
        continue
    if line[0] == '+':
        count += 1
    elif line[0] == '-':
        count -= 1
    else:
        msg = line.split(':', 1)[1]
        total += len(msg) * count
print total
