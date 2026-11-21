class Solution {
public:
    vector<int> findSubtreeSizes(vector<int>& parent, string s) {
        int n = parent.size();
        vector<vector<int>> children(n);
        for (int i = 1; i < n; i++) children[parent[i]].push_back(i);
        vector<int> newParent(parent);
        vector<int> order;
        order.reserve(n);
        vector<vector<int>> stk(26);
        vector<pair<int, int>> st;
        st.push_back({0, 0});
        stk[s[0] - 'a'].push_back(0);
        order.push_back(0);
        while(!st.empty()) {
            auto &[u, idx] = st.back();
            if (idx < (int) children[u].size()) {
                int v = children[u][idx++];
                int c = s[v] - 'a';
                if (!stk[c].empty()) newParent[v] = stk[c].back();
                stk[c].push_back(v);
                order.push_back(v);
                st.push_back({v, 0});

            } else {
                stk[s[u] - 'a'].pop_back();
                st.pop_back();
            }
        }
        vector<int> ans(n , 1);
        for (int i = n - 1; i >= 1; i--) {
            int v = order[i];
            ans[newParent[v]] += ans[v];
        }
        return ans;
    }
};
