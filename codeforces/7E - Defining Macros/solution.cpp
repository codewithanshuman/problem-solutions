#include <bits/stdc++.h>
using namespace std;

map<string,int> mp;
string s;
size_t pos;

int parseExpr();

int comb(int a, char op, int b) {
    if (a == 1 || b == 1) return 1;
    if (op == '+') return 3;
    if (op == '-') return b == 3 ? 1 : 3;
    if (op == '*') return (a == 3 || b == 3) ? 1 : 4;
    return (a == 3 || b == 3 || b == 4) ? 1 : 4; // '/'
}

int parseFactor() {
    if (s[pos] == '(') {
        pos++;
        int r = parseExpr();
        pos++; // ')'
        return r == 1 ? 1 : 2;
    }
    string t;
    while (pos < s.size() && isalnum((unsigned char)s[pos])) t += s[pos++];
    auto it = mp.find(t);
    if (it != mp.end()) return it->second;
    return 2;
}

int parseTerm() {
    int r = parseFactor();
    while (pos < s.size() && (s[pos] == '*' || s[pos] == '/')) {
        char op = s[pos++];
        int b = parseFactor();
        r = comb(r, op, b);
    }
    return r;
}

int parseExpr() {
    int r = parseTerm();
    while (pos < s.size() && (s[pos] == '+' || s[pos] == '-')) {
        char op = s[pos++];
        int b = parseTerm();
        r = comb(r, op, b);
    }
    return r;
}

int evalStr(const string& e) {
    s.clear();
    for (char c : e) if (c != ' ' && c != '\t' && c != '\r') s += c;
    pos = 0;
    return parseExpr();
}

int main() {
    string line;
    getline(cin, line);
    int n = stoi(line);
    while (n--) {
        getline(cin, line);
        size_t i = 0;
        while (line[i] == ' ') i++;
        i++; // '#'
        while (line[i] == ' ') i++;
        i += 6; // "define"
        while (line[i] == ' ') i++;
        string name;
        while (i < line.size() && isalpha((unsigned char)line[i])) name += line[i++];
        mp[name] = evalStr(line.substr(i));
    }
    getline(cin, line);
    cout << (evalStr(line) == 1 ? "Suspicious" : "OK") << endl;
}
