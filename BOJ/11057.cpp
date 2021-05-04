#include <iostream>
#include <cmath>
#include <cstdio>
using namespace std;
#define mod 10007

int upNumber(int n)
{
    int dp[1001][10];
    for (int i = 0; i < 10; i++)
    {
        dp[1][i] = 1;
    }
    for (int i = 2; i <= n; i++)
    {
        dp[i][0] = 1;
        for (int j = 1; j < 10; j++)
        {
            dp[i][j] = (dp[i][j - 1] + dp[i - 1][j]) % mod;
        }
    }

    int ans = 0;
    for (int i = 0; i < 10; i++)
    {
        ans += dp[n][i];
    }
    ans %= mod;

    return ans;
}

int main()
{
    int N;
    cin >> N;
    printf("%d", upNumber(N));
}
