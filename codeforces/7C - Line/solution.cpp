#include <bits/stdc++.h>
using namespace std;
typedef long long ll;


ll ext(ll a, ll b, ll &x, ll &y) {
    if (b == 0) { x = 1; y = 0; return a; }
    ll x1, y1;
    ll g = ext(b, a % b, x1, y1);
    x = y1;
    y = x1 - (a / b) * y1;
    return g;
}

int main() {
    ll A, B, C;
    cin >> A >> B >> C;

    ll x, y;
    ll g = ext(llabs(A), llabs(B), x, y);   
    if (A < 0) x = -x;                     
    if (B < 0) y = -y;

    if (C % g != 0) {
        cout << -1 << endl;
        return 0;
    }

    ll k = -C / g;
    cout << x * k << " " << y * k << endl;
    return 0;
}
