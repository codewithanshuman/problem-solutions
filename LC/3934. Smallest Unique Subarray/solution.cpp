class Solution {
public:
    int smallestUniqueSubarray(vector<int>& nums) {
        int n = nums.size();
        vector<int> sa(n), rk(n), tmp(n), lcp(n, 0);
        for (int i = 0; i < n; i++) {
            sa[i] = i;
            rk[i] = nums[i];
        }
        for (int k = 1;; k <<= 1) {
            auto cmp = [&](int a, int b) {
                if (rk[a] != rk[b]) return rk[a] < rk[b];
                int ra = a + k < n ? rk[a + k] : -1;
                int rb = b + k < n ? rk[b + k] : -1;
                return ra < rb;
            };
            sort(sa.begin(), sa.end(), cmp);
            tmp[sa[0]] = 0;
            for (int i = 1; i < n; i++)
                tmp[sa[i]] = tmp[sa[i - 1]] + (cmp(sa[i - 1], sa[i]) ? 1 : 0);
            rk = tmp;
            if (rk[sa[n - 1]] == n - 1) break;
            
        }
        for (int i = 0, h = 0; i < n; i++) {
            if (rk[i] > 0) {
                int j = sa[rk[i] - 1];
                while (i + h < n && j + h < n && nums[i + h] == nums[j + h]) h++;
                lcp[rk[i]] = h;
                if (h > 0) h--;
            }
             else {
                h = 0;
             }
        }
        int ans = n;
        for (int i = 0; i < n; i++) {
            int prev = i > 0 ? lcp[i] : 0;
            int next = i + 1 < n ? lcp[i + 1] : 0;
            int len = max(prev, next) + 1;
            if (len <= n - sa[i]) ans = min(ans, len);
        }
        return ans;
    }
};
