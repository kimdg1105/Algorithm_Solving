#include <iostream>
using namespace std;

int paper[100][100] = {
    0,
};

int main()
{
    int n;
    cin >> n;

    int result = 0;

    for (int i = 0; i < n; i++)
    {
        int x, y;
        cin >> x >> y;
        for (int j = 0; j < 10; j++)
        {
            for (int k = 0; k < 10; k++)
            {
                paper[j + x][k + y] = 1;
            }
        }
    }

    for (int i = 0; i < 100; i++)
    {
        for (int j = 0; j < 100; j++)
        {
            if (paper[i][j] == 1)
            {
                result++;
            }
        }
    }

    cout << result << '\n';
}