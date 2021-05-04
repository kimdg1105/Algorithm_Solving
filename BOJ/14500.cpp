#include <iostream>
#include <vector>
#define MAX 1000
using namespace std;

int N, M;
int arr[MAX][MAX] = {
    0,
};

void cal(int x, int y, int cnt, int sum)
{
    if (x > N || y > M)
    {
        return;
    }
    if (cnt == 4)
    {
        return;
    }
    
}

int main()
{

    int num;
    cin >> N >> M;

    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < M; j++)
        {
            cin >> arr[i][j];
        }
    }

    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < M; j++)
        {
            cout << arr[i][j] << ' ';
        }
        cout << '\n';
    }
}