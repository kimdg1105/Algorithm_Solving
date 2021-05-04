#include <iostream>
#include <stdio.h>
#include <vector>
#include <queue>
#include <stack>
#include <algorithm>
using namespace std;

void visit(int start)
{
    cout << start << " ";
}

void dfs(int start, vector<int> graph[], bool check[])
{
    stack<int> s;
    s.push(start);
    check[start] = true;
    visit(start);

    while (!s.empty())
    {
        int current = s.top();
        s.pop();
        for (int i = 0; i < graph[current].size(); i++)
        {
            int next_node = graph[current][i];

            if (check[next_node] == false)
            {
                visit(next_node);
                check[next_node] = true;
                s.push(current);
                s.push(next_node);
                break;
            }
        }
    }
}

void bfs(int start, vector<int> graph[], bool check[])
{
    queue<int> q;

    q.push(start);
    check[start] = true;

    while (!q.empty())
    {
        int temp = q.front();
        q.pop();
        visit(temp);

        for (int i = 0; i < graph[temp].size(); i++)
        {
            if (check[graph[temp][i]] == false)
            {
                q.push(graph[temp][i]);
                check[graph[temp][i]] = true;
            }
        }
    }
}

int main()
{
    int N, M, V;

    cin >> N >> M >> V;
    vector<int> graph[N + 1];
    bool check[N + 1];

    fill(check, check + N + 1, false);

    int key, value;
    for (int i = 0; i < M; i++)
    {
        cin >> key >> value;
        graph[key].push_back(value);
        graph[value].push_back(key);
    }

    for (int i = 1; i <= N; i++)
    {
        sort(graph[i].begin(), graph[i].end());
    }

    dfs(V, graph, check);
    fill(check, check + N + 1, false);
    cout << '\n';
    bfs(V, graph, check);
}