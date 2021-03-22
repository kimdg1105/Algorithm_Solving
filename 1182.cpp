#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int N, S;
vector<int> v;
int cnt = 0;

void cal(int idx, int sum)
{
    if (idx >= N)
    {
        return;
    }
    if (sum + v[idx] == S)
    {
        cnt++;
    }

    cal(idx + 1, sum + v[idx]);
    cal(idx + 1, sum);
}

int main()
{

    cin >> N >> S;

    int num;
    for (int i = 0; i < N; i++)
    {
        cin >> num;
        v.push_back(num);
    }

    sort(v.begin(), v.end());

    cal(0, 0);

    cout << cnt << '\n';
}