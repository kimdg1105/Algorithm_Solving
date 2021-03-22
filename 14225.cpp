#include <iostream>
#include <vector>
#include <algorithm>
#define MAX 2000000
using namespace std;

vector<int> v;
vector<int> sum_v;
bool flag[MAX] = {false};
int N;

void cal(int idx, int sum)
{
    if (idx == N)
    {
        flag[sum] = true;
        return;
    }
    cal(idx + 1, sum);
    cal(idx + 1, sum + v[idx]);
    sum += v[idx];
    sum_v.push_back(sum);
}

int main()
{
    int ans;
    cin >> N;

    int num;
    for (int i = 0; i < N; i++)
    {
        cin >> num;
        v.push_back(num);
    }
    sort(v.begin(), v.end());
    cal(0, 0);

    sort(sum_v.begin(), sum_v.end());

    // for (int i = 0; i < sum_v.size(); i++)
    // {
    //     cout << sum_v[i] << " ";
    // }
    // cout << '\n';

    int idx = 0;
    while (1)
    {
        if (flag[idx] != true)
        {
            cout << idx << '\n';
            break;
        }
        idx++;
    }
}