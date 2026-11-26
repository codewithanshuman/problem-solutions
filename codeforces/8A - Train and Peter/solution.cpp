#include <bits/stdc++.h>
using namespace std;

static bool check(const string& s, const string& a, const string& b) {
    size_t p = s.find(a);
    if (p == string::npos) return false;
    return s.find(b, p + a.size()) != string::npos;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s, a, b;
    cin >> s >> a >> b;

    bool fwd = check(s, a, b);
    reverse(s.begin(), s.end());
    bool bwd = check(s, a, b);

    if (fwd && bwd) cout << "both";
    else if (fwd) cout << "forward";
    else if (bwd) cout << "backward";
    else cout << "fantasy";
    cout << "\n";
    return 0;
}
