#include <bits/stdc++.h>
using namespace std;

int main() {
    string s;
    cin >> s;

    set<pair<int,int>> vis;
    int x = 0, y = 0;
    vis.insert({x, y});

    int dx[4] = {1, -1, 0, 0};
    int dy[4] = {0, 0, 1, -1};

    for (char c : s) {
        int px = x, py = y;  
        if (c == 'L') x--;
        else if (c == 'R') x++;
        else if (c == 'U') y++;
        else y--;

        
        if (vis.count({x, y})) {
            cout << "BUG" << endl;
            return 0;
        }

       
        for (int d = 0; d < 4; d++) {
            int nx = x + dx[d], ny = y + dy[d];
            if (nx == px && ny == py) continue;
            if (vis.count({nx, ny})) {
                cout << "BUG" << endl;
                return 0;
            }
        }

        vis.insert({x, y});
    }

    cout << "OK" << endl;
    return 0;
}
