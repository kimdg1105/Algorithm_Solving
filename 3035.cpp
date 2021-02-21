#include <iostream>
using namespace std;

int main()
{
    int r, c;
    int zr, zc;
    cin >> r >> c >> zr >> zc;
    int cnt = 0;

    char arr[r + 1][c + 1];

    for (int i = 0; i < r; i++)
    {
        for (int j = 0; j < c; j++)
        {
            cin >> arr[i][j];
        }
    }

    int idx = 0;

    for (int i = 0; i < r; i++)
    {
        for (int w = 0; w < zr; w++)
        {
            for (int j = 0; j < c; j++)
            {
                for (int q = 0; q < zc; q++)
                {
                    cout << arr[i][j];
                }
            }
            cout << '\n';
        }
    }
}