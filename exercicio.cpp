#include <bits/stdc++.h>
using namespace std;

const int oo = 1e9;

vector<int> bfs(int s, int N, vector<vector<int>> &adj) {
    vector<int> dist(N + 1, -1);
    queue<int> q;

    dist[s] = 0;
    q.push(s);

    while (!q.empty()) {
        int u = q.front();
        q.pop();

        for (auto v : adj[u]) {
            if (dist[v] == -1) { 
                dist[v] = dist[u] + 1;
                q.push(v);
            }
        }
    }

    return dist; 
}

int main() {
    int n, value;
    cin >> n;

    vector<vector<int>> pi(n + 1);

    for (int i = 1; i <= n; i++) {
        cin >> value;

        if (value != -1) {
            pi[value].push_back(i);
        }
    }

    int altmax = 0;

    for (int root = 1; root <= n; ++root) {
        vector<int> height = bfs(root, n, pi);
    }



    return 0;
}

