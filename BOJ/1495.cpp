#include <iostream>
using namespace std;

int dp[101][1001];

int main()
{
    int N, S, M;
    cin >> N >> S >> M;

    int v[N];
    for (int i = 1; i <= N; i++)
    {
        cin >> v[i];
    }

    if (S + v[1] <= M)
    {
        dp[1][S + v[1]] = 1;
    }
    if (S - v[1] >= 0)
    {
        dp[1][S - v[1]] = 1;
    }

    for (int i = 2; i <= N; i++)
    {
        for (int j = 0; j <= M; j++)
        {
            if (dp[i - 1][j] == 1)
            {
                if (j + v[i] <= M)
                {
                    dp[i][j + v[i]] = 1;
                }
                if (j - v[i] >= 0)
                {
                    dp[i][j - v[i]] = 1;
                }
            }
        }
    }
    int max = -1;

    for (int k = M; k >= 0; k--)
    {
        if (dp[N][k] == 1)
        {
            cout << k << endl;
            return 0;
        }
    }
    cout << -1 << endl;
    return 0;
}