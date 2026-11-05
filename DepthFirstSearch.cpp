#include <iostream>
#include <vector>
using namespace std;

vector<int> graph[10];
bool visited[10];

void DFS(int node)
{
    visited[node] = true;

    cout << node << " ";

    for (int i = 0; i < graph[node].size(); i++)
    {
        int next = graph[node][i];

        if (!visited[next])
        {
            DFS(next);
        }
    }
}

int main()
{
    int vertices, edges;

    cout << "Enter number of vertices: ";
    cin >> vertices;

    cout << "Enter number of edges: ";
    cin >> edges;

    cout << "Enter edges:" << endl;

    for (int i = 0; i < edges; i++)
    {
        int u, v;
        cin >> u >> v;

        graph[u].push_back(v);
        graph[v].push_back(u);
    }

    for (int i = 0; i < vertices; i++)
    {
        visited[i] = false;
    }

    int start;
    cout << "Enter starting vertex: ";
    cin >> start;

    cout << "DFS Traversal: ";
    DFS(start);

    return 0;
}