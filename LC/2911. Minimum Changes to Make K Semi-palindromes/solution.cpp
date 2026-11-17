class Solution {
public:
    int minimumChanges(string s, int k) {
        int n = s.size();
        const int INF = 1e9;
        vector<vector<int>> divs(n + 1);
        for (int len = 2; len <= n; len++)
            for (int d = 1; d < len; d++)
                if (len % d == 0) divs[len].push_back(d);
        vector<vector<int>> cost(n, vector<int>(n, INF));
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                int len = j - i + 1;
                int best = INF;
                for (int d : divs[len]) {
                    int changes = 0;
                    int m = len / d;
                    for (int r = 0; r < d; r++) {
                        int lo = 0, hi = m - 1;
                        while (lo < hi) {
                            if (s[i + r + lo * d] != s[i + r + hi * d]) changes++;
                            lo++; hi--;
                        }
                    }
                    best = min(best, changes);
                }
                cost[i][j] = best;
            }
        }
        vector<vector<int>> dp(k + 1, vector<int>(n + 1, INF));
        dp[0][0] = 0;
        for (int p = 1; p <= k; p++) {
            for (int i = 2 * p; i <= n; i++) {
                for (int j = 2 * (p - 1); j <= i - 2; j++) {
                    if (dp[p - 1][j] == INF || cost[j][i - 1] == INF) continue;
                    dp[p][i] = min(dp[p][i], dp[p - 1][j] + cost[j][i - 1]);
                }
            }
        }
        return dp[k][n];
    }
};
