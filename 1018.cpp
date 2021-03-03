#include <iostream>
#include <string>
#include <algorithm>
#define MAX 8
using namespace std;

char chess[51][51];

char white[8][8] = {
    'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B',
    'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W',
    'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B',
    'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W',
    'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B',
    'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W',
    'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B',
    'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'};
char black[8][8] = {
    'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W',
    'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B',
    'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W',
    'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B',
    'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W',
    'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B',
    'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W',
    'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'};

int W_cnt(int x, int y)
{
    int cnt = 0;
    for (int i = 0; i < MAX; i++)
    {
        for (int j = 0; j < MAX; j++)
        {
            if (chess[x + i][y + j] != white[i][j])
            {
                cnt++;
            }
        }
    }
    return cnt;
}
int B_cnt(int x, int y)
{
    int cnt = 0;
    for (int i = 0; i < MAX; i++)
    {
        for (int j = 0; j < MAX; j++)
        {

            if (chess[x + i][y + j] != black[i][j])
            {

                cnt++;
            }
        }
    }
    return cnt;
}

int main()
{
    int N, M;

    cin >> N >> M;

    // Input
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < M; j++)
        {
            cin >> chess[i][j];
        }
    }

    // Output
    int min_val = 64;
    for (int i = 0; i + MAX <= N; i++)
    {
        for (int j = 0; j + MAX <= M; j++)
        {
            int cnt;
            cnt = min(W_cnt(i, j), B_cnt(i, j));
            if (cnt < min_val)
            {
                min_val = cnt;
            }
        }
    }
    cout << min_val << '\n';
}