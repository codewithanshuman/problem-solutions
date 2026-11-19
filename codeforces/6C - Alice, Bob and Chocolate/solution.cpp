#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> t(n);
    for (auto &x : t) cin >> x;

    int i = 0, j = n - 1;
    int ta = 0, tb = 0;
    int a = 0, b = 0;

    while (i <= j) {
        if (ta <= tb) {
            ta += t[i++];
            a++;
        } else {
            tb += t[j--];
            b++;
        }
    }

    cout << a << " " << b;
    return 0;
}
