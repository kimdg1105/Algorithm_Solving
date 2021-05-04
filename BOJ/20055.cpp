#include <iostream>
#include <vector>
#include <deque>
#include <utility>
using namespace std;

typedef pair<int, bool> spec;
typedef pair<int, spec> mypair;
int N, K;

deque<mypair> belt;

deque<mypair> spinBelt()
{
    mypair temp = belt.back();
    belt.pop_back();
    belt.push_front(temp);

    return belt;
}

void moveRobot()
{
    for (int i = belt.size(); i >= 0; i--)
    {
        if (belt[i].second.second == true)
        {

            if (belt[i + 1].second.first > 0 && belt[i + 1].second.second == false)
            {
                belt[i + 1].second.second = true;
                belt[i].second.second = false;
                belt[i + 1].second.first--;
            }
        }
    }
}

void addRobot()
{

    if (belt.front().second.second == false && belt.front().second.first > 0)
    {
        belt.front().second.second = true;
        belt.front().second.first--;
    }
}

int check()
{
    int limit = 0;
    for (int i = 0; i < belt.size(); i++)
    {
        if (belt[i].second.first == 0)
        {
            limit++;
        }
    }
    return limit;
}

int main()
{
    cin >> N >> K;
    int num;
    for (int i = 0; i < 2 * N; i++)
    {
        cin >> num;
        belt.push_back(make_pair(i + 1, make_pair(num, false)));
    }

    int cnt = 1;

    while (1)
    {
        spinBelt();
        if (belt[N - 1].second.second == true)
        {
            belt[N - 1].second.second = false;
        }
        moveRobot();
        if (belt[N - 1].second.second == true)
        {
            belt[N - 1].second.second = false;
        }
        addRobot();

        if (check() >= K)
        {
            cout << cnt << endl;
            break;
        }
        cnt++;
    }
}