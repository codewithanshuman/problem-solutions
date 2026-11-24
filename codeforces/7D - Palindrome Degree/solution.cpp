#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    cin >> s;
    int n = s.size();

    vector<int> d1(n), d2(n);


    for (int i = 0, l = 0, r = -1; i < n; i++) {
        int k = (i > r) ? 1 : min(d1[l + r - i], r - i + 1);
        while (i - k >= 0 && i + k < n && s[i - k] == s[i + k]) k++;
        d1[i] = k;
        if (i + k - 1 > r) l = i - k + 1, r = i + k - 1;
    }


    for (int i = 0, l = 0, r = -1; i < n; i++) {
        int k = (i > r) ? 0 : min(d2[l + r - i + 1], r - i + 1);
        while (i + k < n && i - k - 1 >= 0 && s[i + k] == s[i - k - 1]) k++;
        d2[i] = k;
        if (i + k - 1 > r) l = i - k, r = i + k - 1;
    }

    vector<char> pal(n + 1, 0);
    for (int i = 0; i < n; i++) {
        if (d1[i] == i + 1) pal[2 * i + 1] = 1;
        if (i >= 1 && d2[i] == i) pal[2 * i] = 1;
    }

    vector<int> deg(n + 1, 0);
    long long ans = 0;
    for (int i = 1; i <= n; i++) {
        if (pal[i]) {
            deg[i] = deg[i / 2] + 1;
            ans += deg[i];
        }
    }

    cout << ans << "\n";
    return 0;
}
