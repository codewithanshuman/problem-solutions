import sys

lines = [l.rstrip('\r\n') for l in sys.stdin.read().split('\n')]

if lines and lines[-1] == '':
    lines.pop()

w = max(len(l) for l in lines)
out = ['*' * (w + 2)]
left_next = True  

for l in lines:
    diff = w - len(l)
    if diff % 2 == 0:
        left = diff // 2
    else:
        if left_next:
            left = diff // 2          
        else:
            left = diff // 2 + 1      
        left_next = not left_next
    right = diff - left
    out.append('*' + ' ' * left + l + ' ' * right + '*')

out.append('*' * (w + 2))
print '\n'.join(out)
