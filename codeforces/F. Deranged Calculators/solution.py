import sys

def const(x):
    """Build a DC-language expression for the positive integer constant x."""
    if x == 1:
        return "n/n"
    return "(" + "+".join("n" * x) + ")/n"

def geq(i):
    """Indicator expression: evaluates to 1 if n >= i, else 0 (for n in [2, i])."""

  
    return "round(n/({0}+n))".format(const(i))

def solve(k):
    N = k
    fact = const(1)
    for j in range(2, N + 1):
        fact += "*({0}*({1})+n/n)".format(geq(j), const(j - 1))
    e = const(1)
    for i in range(N, 0, -1):
        e = "n/n+n/({0})*({1})".format("+".join("n" * i), e)

  
    return "round({0}/({1}))".format(fact, e)

if __name__ == "__main__":
    k = int(sys.stdin.readline())
  
    print solve(k)
