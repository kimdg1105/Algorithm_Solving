#include <iostream>
#include <cstring>
using namespace std;

int main()
{
    int N, M;
    cin >> N >> M;

    int arr[N + 1][M + 1];
    memset(arr, 0, N * M);

    for (int i = 1; i <= N; i++)
    {
        for (int j = 1; j <= M; j++)
        {
            cin >> arr[i][j];
        }
    }

    int K;
    cin >> K;

    for (int i = 0; i < K; i++)
    {
        int sum = 0;
        int a, b, x, y;
        cin >> a >> b >> x >> y;

        for (int q = a; q <= x; q++)
        {
            for (int w = b; w <= y; w++)
            {
                sum += arr[q][w];
            }
        }
        cout << sum << '\n';
    }
}