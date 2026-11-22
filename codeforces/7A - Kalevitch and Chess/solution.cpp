#include <bits/stdc++.h>
using namespace std;

int main() {
    string g[8];
    for (int i = 0; i < 8; i++) cin >> g[i];

    int rows = 0, cols = 0;
    for (int i = 0; i < 8; i++) {
        if (g[i] == "BBBBBBBB") rows++;
    }
    for (int j = 0; j < 8; j++) {
        bool full = true;
        for (int i = 0; i < 8; i++) {
            if (g[i][j] != 'B') { full = false; break; }
        }
        if (full) cols++;
    }

    if (rows == 8) cout << 8 << endl;
    else cout << rows + cols << endl;
    return 0;
}
