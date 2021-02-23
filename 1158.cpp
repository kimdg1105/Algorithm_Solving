#include <iostream>
#include <queue>
using namespace std;

int main()
{
    int N, K;
    queue<int> q;

    cin >> N >> K;
    for (int i = 1; i <= N; i++)
    {
        q.push(i);
    }
    cout << "<";
    while (1)
    {

        for (int j = 1; j <= K - 1; j++)
        {
            q.push(q.front());
            q.pop();
        }
        cout << q.front();
        q.pop();
        if (q.empty())
        {
            break;
        }
        cout << ", ";
    }
    cout << ">";
}