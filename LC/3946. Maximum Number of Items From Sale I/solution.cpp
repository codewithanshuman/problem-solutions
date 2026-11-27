class Solution {
public:
    int maximumSaleItems(vector<vector<int>>& items, int budget) {
        int n = items.size();
        vector<int> dp(budget + 1, 0);
        for (int i = 0; i < n; i++) {
            int f = items[i][0], p = items[i][1];
            int g = 0;
            for (int j = 0; j < n; j++) {
                if (j != i && items[j][0] % f == 0) g++;
            }
            for (int b = budget; b >= p; b--) {
                dp[b] = max(dp[b], dp[b - p] + 1 + g);
            }
            for (int b = p; b <= budget; b++) {
                dp[b] = max(dp[b], dp[b - p] + 1);
            }

        }
        return dp[budget];
    }
};
