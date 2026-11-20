#include <bits/stdc++.h>
using namespace std;

const int INF = 1e9;
int n, a, b;
int h[16];
int memoV[12][17][17][17];
int memoX[12][17][17][17];
bool vis[12][17][17][17];


int f(int i, int p, int c, int nx) {
    if (i == n - 1) return (p < 0 && c < 0) ? 0 : INF;
    if (vis[i][p + 1][c + 1][nx + 1]) return memoV[i][p + 1][c + 1][nx + 1];

    int best = INF, bestX = 0;
    for (int x = 0; x <= 16; x++) {
        if (p - x * b >= 0) continue;           
        int np = max(c - x * a, -1);
        int nc = max(nx - x * b, -1);
        int nnx = (i + 2 < n) ? h[i + 2] : 0;
        int r = f(i + 1, np, nc, nnx);
        if (r < INF && r + x < best) {
            best = r + x;
            bestX = x;
        }
    }
    vis[i][p + 1][c + 1][nx + 1] = true;
    memoV[i][p + 1][c + 1][nx + 1] = best;
    memoX[i][p + 1][c + 1][nx + 1] = bestX;
    return best;
}

int main() {
    scanf("%d %d %d", &n, &a, &b);
    for (int i = 0; i < n; i++) scanf("%d", &h[i]);

    int total = f(1, h[0], h[1], h[2]);
    printf("%d\n", total);

    // reconstruct
    vector<int> res;
    int i = 1, p = h[0], c = h[1], nx = h[2];
    while (i < n - 1) {
        int x = memoX[i][p + 1][c + 1][nx + 1];
        for (int k = 0; k < x; k++) res.push_back(i + 1);  
        int np = max(c - x * a, -1);
        int nc = max(nx - x * b, -1);
        int nnx = (i + 2 < n) ? h[i + 2] : 0;
        p = np; c = nc; nx = nnx;
        i++;
    }
    for (size_t k = 0; k < res.size(); k++) printf("%d ", res[k]);
    printf("\n");
    return 0;
}
