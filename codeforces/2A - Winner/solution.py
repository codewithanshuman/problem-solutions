n = int(raw_input())
rounds = []
final = {}
for _ in range(n):
    name, score = raw_input().split()
    score = int(score)
    rounds.append((name, score))
    final[name] = final.get(name, 0) + score

m = max(final.values())
candidates = set(k for k, v in final.items() if v == m)

cur = {}
for name, score in rounds:
    cur[name] = cur.get(name, 0) + score
    if name in candidates and cur[name] >= m:
        print(name)
        break
