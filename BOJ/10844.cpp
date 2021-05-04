#include <iostream>
#include <cstring>
#define MAX 101
#define MOD 1000000000
using namespace std;

int cache[MAX][10];

long long dp(int n)
{
    for (int i = 1; i < 10; i++)
    {
        cache[1][i] = 1;
    }
    for (int i = 2; i <= n; i++)
    {
        for (int j = 0; j < 10; j++)
        {
            if (j == 0)
            {
                cache[i][j] = cache[i - 1][1];
            }
            else if (j == 9)
            {
                cache[i][j] = cache[i - 1][8];
            }
            else
            {
                cache[i][j] = cache[i - 1][j - 1] + cache[i - 1][j + 1];
            }
            cache[i][j] %= MOD;
        }
    }
    long long result = 0;
    for (int i = 0; i < 10; i++)
    {
        result += cache[n][i];
        result %= MOD;
    }
    return result;
}

int main()
{
    int N;
    memset(cache, 0, sizeof(cache));
    cin >> N;
    long long result = dp(N);
    cout << result << '\n';
}