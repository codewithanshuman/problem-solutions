#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, k;
    scanf("%d %d", &n, &k);
    vector<int> h(n);
    for (auto &x : h) scanf("%d", &x);

    deque<int> mx, mn;
    int l = 0, best = 0;
    vector<pair<int,int>> res;

    for (int r = 0; r < n; r++) {
        while (!mx.empty() && h[mx.back()] <= h[r]) mx.pop_back();
        mx.push_back(r);
        while (!mn.empty() && h[mn.back()] >= h[r]) mn.pop_back();
        mn.push_back(r);

        while (h[mx.front()] - h[mn.front()] > k) {
            l++;
            if (mx.front() < l) mx.pop_front();
            if (mn.front() < l) mn.pop_front();
        }

        int len = r - l + 1;
        if (len > best) {
            best = len;
            res.clear();
            res.push_back({l + 1, r + 1});
        } else if (len == best) {
            res.push_back({l + 1, r + 1});
        }
    }

    printf("%d %d\n", best, (int)res.size());
    for (auto &p : res) printf("%d %d\n", p.first, p.second);
    return 0;
}
