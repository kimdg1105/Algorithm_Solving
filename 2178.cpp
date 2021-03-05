#include <iostream>
using namespace std;

int main()
{
    int N, M;
    cin >> N >> M;

    int maze[N + 1][M + 1];

    for (int i = 0; i < N; i++)
    {
        for (int j = 0; i < M; j++)
        {
            cin >> maze[i][j];
        }
    }
}