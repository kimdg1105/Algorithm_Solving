#include <iostream>
#include <string>
#include <deque>
#include <vector>
#include <cmath>
using namespace std;

int main()
{
    int N, M;
    int start = 0;
    deque<int> dq;
    int cnt = 0;
    int num;
    int idx = 0;

    cin >> N >> M;

    //init
    for (int i = 1; i <= N; i++)
    {
        dq.push_back(i);
    }

    for (int i = 0; i < M; i++)
    {

        cin >> num;

        for (int j = 0; j < dq.size(); j++)
        {
            if (dq[j] == num)
            {
                idx = j;
                break;
            }
        }

        if (idx < dq.size() - idx)
        {
            while (1)
            {
                if (dq.front() == num)
                {
                    dq.pop_front();
                    break;
                }
                cnt++;
                dq.push_back(dq.front());
                dq.pop_front();
            }
        }
        else
        {
            while (1)
            {
                if (dq.front() == num)
                {
                    dq.pop_front();
                    break;
                }
                cnt++;
                dq.push_front(dq.back());
                dq.pop_back();
            }
        }
    }

    cout << cnt << endl;
}