#include <bits/stdc++.h>
using namespace std;

const int oo = 1e9;

vector<int> bfs(int s, int N, vector<vector<int>> &adj) {
    // armazena a distância de s para os outros nós
    vector<int> dist(N + 1, -1);
    queue<int> q;

    dist[s] = 0;
    q.push(s);

    while (!q.empty()) {
        int u = q.front();
        q.pop();

        for (auto v : adj[u]) {
            if (dist[v] == -1) { // ainda não visitado
                dist[v] = dist[u] + 1; // atualiza a distância
                q.push(v);
            }
        }
    }

    return dist; // retorna distancia
}

int main() {
    int n, value;
    cin >> n;

    // lista de adjacencia 
    vector<vector<int>> pi(n + 1);

    // leitura das relações de funcionários, até n 
    for (int i = 1; i <= n; i++) {
        cin >> value;

        if (value != -1) {
            pi[value].push_back(i);
        }
    }

    int altmax = 0;

    // calculo para cada funcionário
    for (int root = 1; root <= n; ++root) {
        // cria uma bfs para calcular a distâncias 
        vector<int> height = bfs(root, n, pi);
        // encontra ao número de camadas da árvore ( altura)
        int x = *max_element(height.begin(), height.end());
        altmax = max(altmax, x);
    }

    // imprime o número de camadas
    cout << altmax+1 << endl;

    return 0;
}

