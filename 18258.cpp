#include <iostream>
#include <queue>
using namespace std;

int main()
{
    int N, K;
    int num;
    queue<int> q;

    cin >> N >> K;

    for (int i = 1; i <= N; i++)
    {

        q.push(i);
    }

    cout << "<";
    while (q.size() != 0)
    {
        int temp;
        for (int i = 0; i < K - 1; i++)
        {
            temp = q.front();
            q.push(temp);
            q.pop();
        }

        cout << q.front();
        q.pop();
        if (q.size() != 0)
        {
            cout << ", ";
        }
    }
    cout << ">";
}