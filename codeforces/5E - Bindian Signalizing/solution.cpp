#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    scanf("%d", &n);
    vector<int> a(n), b(n);
    for (auto &x : a) scanf("%d", &x);

    int idx = max_element(a.begin(), a.end()) - a.begin();
    for (int i = 0; i < n; i++) b[i] = a[(idx + i) % n];

    long long ans = 0;
    vector<pair<int, int>> st;
    st.push_back({b[0], 1});

    for (int i = 1; i < n; i++) {
        while (st.back().first < b[i]) {
            ans += st.back().second;
            st.pop_back();
        }
        if (st.back().first == b[i]) {
            int c = st.back().second;
            ans += c;
            st.pop_back();
            if (!st.empty()) ans++;
            st.push_back({b[i], c + 1});
        } else {
            ans++;
            st.push_back({b[i], 1});
        }
    }

    for (size_t j = 1; j < st.size(); j++) {
        if (j == 1 && st[0].second == 1) continue;
        ans += st[j].second;
    }

    printf("%lld\n", ans);
    return 0;
}
