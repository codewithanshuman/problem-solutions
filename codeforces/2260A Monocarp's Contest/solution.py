t = int(raw_input())
for _ in range(t):
    n = int(raw_input())
    a = list(map(int, raw_input().split()))
    if a.count(0) < 2:
        print(-1)
    else:
        print(a[0] + a[-1])
