#include <bits/stdc++.h>
using namespace std;

int main() {
    int s[4];
    for (int i = 0; i < 4; i++) cin >> s[i];

    bool triangle = false, segment = false;

    for (int skip = 0; skip < 4; skip++) {
        vector<int> t;
        for (int i = 0; i < 4; i++)
            if (i != skip) t.push_back(s[i]);
        sort(t.begin(), t.end());

        if (t[0] + t[1] > t[2]) triangle = true;
        else if (t[0] + t[1] == t[2]) segment = true;
    }

    if (triangle) cout << "TRIANGLE";
    else if (segment) cout << "SEGMENT";
    else cout << "IMPOSSIBLE";
    return 0;
}
