#include <iostream>
#include <deque>
#include <vector>
using namespace std;

int main()
{
    deque<int> dq;
    int N;
    vector<int> seq;

    cin >> N;

    for (int i = 0; i < N; i++)
    {
        int num;
        cin >> num;
        dq.push_back(num);
    }

    int idx = 0;
    int value;
    value = dq.front();
    seq.push_back(1);
    dq.pop_front();

    while (dq.size())
    {
        if (value > 0)
        {
            for (int k = 0; k < value; k++)
            {
                dq.push_back(dq.front());
                dq.pop_front();
            }
            value = dq.front();
        }
        else
        {
        }

        seq.push_back(idx + 1);
        idx = q.front();
        q.pop();
    }
}