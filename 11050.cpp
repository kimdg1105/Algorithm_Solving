#include <iostream>
#include <cstring>
using namespace std;

int arr[2000][2000];

int binomial(int n, int k)
{

    if (n == k || k == 0)
    {
        return 1;
    }
    else if (arr[n][k] > -1)
    {
        return arr[n][k] % 10007;
    }
    else
    {
        arr[n][k] = binomial(n - 1, k) + binomial(n - 1, k - 1);
        return arr[n][k] % 10007;
    }
}

int main()
{
    int N, K;
    cin >> N >> K;
    memset(arr, -1, sizeof(arr));
    int result = binomial(N, K);
    cout << result << '\n';
}