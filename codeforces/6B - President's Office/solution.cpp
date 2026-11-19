#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, m;
    char c;
    cin >> n >> m >> c;

    vector<string> g(n);
    for (int i = 0; i < n; i++) cin >> g[i];

    set<char> deputies;
    int dx[] = {1, -1, 0, 0};
    int dy[] = {0, 0, 1, -1};

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (g[i][j] != c) continue;
            for (int d = 0; d < 4; d++) {
                int x = i + dx[d], y = j + dy[d];
                if (x < 0 || x >= n || y < 0 || y >= m) continue;
                if (g[x][y] != '.' && g[x][y] != c)
                    deputies.insert(g[x][y]);
            }
        }
    }

    cout << deputies.size();
    return 0;
}
