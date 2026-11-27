#include <bits/stdc++.h>
using namespace std;

int main() {
    int xs, ys, n;
    scanf("%d %d %d", &xs, &ys, &n);
    vector<int> x(n), y(n);
    for (int i = 0; i < n; i++) scanf("%d %d", &x[i], &y[i]);

    auto sq = [](int a, int b) { return a * a + b * b; };
    vector<int> d0(n);
    vector<vector<int>> d(n, vector<int>(n));
    for (int i = 0; i < n; i++) {
        d0[i] = sq(x[i] - xs, y[i] - ys);
        for (int j = 0; j < n; j++)
            d[i][j] = sq(x[i] - x[j], y[i] - y[j]);
    }

    int full = (1 << n) - 1;
    const int INF = INT_MAX;
    vector<int> dp(1 << n, INF);
    vector<int> par(1 << n, -1);  
    dp[0] = 0;

    for (int mask = 0; mask < full; mask++) {
        if (dp[mask] == INF) continue;
        int i = 0;
        while (mask >> i & 1) i++;  


        int nm = mask | (1 << i);
        int c = dp[mask] + 2 * d0[i];
        if (c < dp[nm]) { dp[nm] = c; par[nm] = mask; }


        for (int j = i + 1; j < n; j++) {
            if (mask >> j & 1) continue;
            int nm2 = mask | (1 << i) | (1 << j);
            int c2 = dp[mask] + d0[i] + d[i][j] + d0[j];
            if (c2 < dp[nm2]) { dp[nm2] = c2; par[nm2] = mask; }
        }
    }

    printf("%d\n", dp[full]);


    vector<vector<int>> trips;
    int m = full;
    while (m) {
        int p = par[m];
        int diff = m ^ p;
        vector<int> t;
        for (int b = 0; b < n; b++)
            if (diff >> b & 1) t.push_back(b + 1);
        trips.push_back(t);
        m = p;
    }

    printf("0");
    for (auto &t : trips) {
        for (int v : t) printf(" %d", v);
        printf(" 0");
    }
    printf("\n");
    return 0;
}
