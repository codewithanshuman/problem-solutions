import sys

s = sys.stdin.readline().strip()
stack = [-1]
best = 0
cnt = 1
for i in range(len(s)):
    if s[i] == '(':
        stack.append(i)
    else:
        stack.pop()
        if not stack:
            stack.append(i)
        else:
            length = i - stack[-1]
            if length > best:
                best = length
                cnt = 1
            elif length == best:
                cnt += 1
print("%d %d" % (best, cnt))
