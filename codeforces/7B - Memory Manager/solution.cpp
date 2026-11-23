#include <bits/stdc++.h>
using namespace std;

int main() {
    int t, m;
    cin >> t >> m;
    vector<int> mem(m, 0);
    int nextId = 0;

    while (t--) {
        string op;
        cin >> op;
        if (op == "alloc") {
            int n;
            cin >> n;
            int start = -1;
            for (int i = 0; i + n <= m && start == -1; i++) {
                bool ok = true;
                for (int j = i; j < i + n; j++) {
                    if (mem[j] != 0) { ok = false; break; }
                }
                if (ok) start = i;
            }
            if (start == -1) {
                cout << "NULL\n";
            } else {
                ++nextId;
                for (int j = start; j < start + n; j++) mem[j] = nextId;
                cout << nextId << "\n";
            }
        } else if (op == "erase") {
            long long x;
            cin >> x;
            bool found = false;
            if (x > 0) {
                for (int i = 0; i < m; i++) {
                    if (mem[i] == x) { mem[i] = 0; found = true; }
                }
            }
            if (!found) cout << "ILLEGAL_ERASE_ARGUMENT\n";
        } else { // defragment
            int w = 0;
            for (int i = 0; i < m; i++) {
                if (mem[i] != 0) mem[w++] = mem[i];
            }
            while (w < m) mem[w++] = 0;
        }
    }
    return 0;
}
