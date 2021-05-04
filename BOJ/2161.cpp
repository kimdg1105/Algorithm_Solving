#include <iostream>
#include <queue>
using namespace std;

int main()
{
    int N;
    queue<int> q;
    cin >> N;
    for (int i = 1; i <= N; i++)
    {
        q.push(i);
    }

    while (1)
    {
        if (q.size() == 1)
        {
            cout << q.front() << '\n';
            break;
        }
        cout << q.front() << ' ';
        q.pop();
        q.push(q.front());
        q.pop();
    }
}