#include <iostream>
#include <queue>
using namespace std;

int main()
{
    int T;

    cin >> T;

    for (int t = 0; t < T; t++)
    {
        int idx = 0;
        int N, M;
        int max = 0;
        queue<pair<int, int> > q;
        int weight;
        int priority[10] = {
            0,
        };

        cin >> N >> M;
        for (int i = 0; i < N; i++)
        {
            cin >> weight;
            q.push(make_pair(i, weight));
            priority[weight]++;
        }

        while (1)
        {
            for (int i = 9; i > 0; i--)
            {
                if (priority[i] != 0)
                {
                    max = i;
                    break;
                }
            }

            pair<int, int> p = q.front();

            if (p.second == max)
            {
                if (p.first == M)
                {
                    idx++;
                    cout << idx << '\n';
                    break;
                }
                q.pop();
                idx++;
                priority[max]--;
            }
            else
            {
                q.push(q.front());
                q.pop();
            }
        }
    }
}