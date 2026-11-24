class Solution {
public:
    int maxLength(vector<int>& nums) {
        int n = nums.size();
        int ans = 0;
        for (int i = 0; i < n; i++) {
            long long prod = 1;
            long long g = 0;
            long long l = 1;
            for (int j = i; j < n; j++) {
                prod *= nums[j];
                if (prod > 1000000LL) break;
                g = __gcd(g, (long long)nums[j]);
                l = l / __gcd(l, (long long)nums[j]) * nums[j];
                if (prod == l * g) {
                    ans = max(ans, j - i + 1);
                }
            }
        }
        return ans;

    }
};
