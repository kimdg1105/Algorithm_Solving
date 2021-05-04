#include <iostream>
#include <deque>
#include <vector>
using namespace std;

int main()
{
    int N;
    vector<int> v;
    deque<pair<int, int> > dq;

    cin >> N;

    int seq;
    for (int i = 1; i <= N; i++)
    {
        cin >> seq;
        dq.push_back(make_pair(i, seq));
    }

    int start = dq.front().second;
    cout << dq.front().first << " ";
    dq.pop_front();

    while (!dq.empty())
    {
        if (start > 0)
        {
            for (int i = 0; i < start; i++)
            {
                int f = dq.front().first;
                int s = dq.front().second;

                pair<int, int> temp = make_pair(f, s);
                dq.push_back(temp);
                dq.pop_front();
            }
            start = dq.back().second;
            cout << dq.back().first << " ";
            dq.pop_back();
        }
        else
        {
            for (int i = 0; i > start; i--)
            {
                int f = dq.back().first;
                int s = dq.back().second;

                pair<int, int> temp = make_pair(f, s);
                dq.push_front(temp);
                dq.pop_back();
            }
            start = dq.front().second;
            cout << dq.front().first << " ";
            dq.pop_front();
        }
    }
}