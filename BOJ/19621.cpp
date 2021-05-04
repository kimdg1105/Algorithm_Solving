#include <iostream>
#include <algorithm>
using namespace std;

#define MAX 150000

int main()
{
    int N;
    cin >> N;
    int start[MAX], end[MAX], num[MAX];
    for (int i = 0; i < N; i++)
    {
        cin >> start[i] >> end[i] >> num[i];
    }
    int dp[MAX] = {0};

    for (int j = 0; j < N; j++)
    {
        if (j == 0 || j == 1)
        {
            dp[j] = num[j];
        }
        else if (j == 2)
        {
            dp[j] = dp[0] + num[j];
        }
        else
        {
            dp[j] = max(dp[j - 3] + num[j], dp[j - 2] + num[j]);
        }
    }
    int result = 0;
    if (N == 1)
    {
        result = dp[0];
    }
    else
    {
        result = max(dp[N - 1], dp[N - 2]);
    }

    cout << result << endl;
}