#include <iostream>
using namespace std;

int main()
{
    int matrix[101][101] = {
        0,
    };
    int result = 0;

    for (int i = 0; i < 4; i++)
    {
        int x1, x2;
        int y1, y2;
        cin >> x1 >> x2 >> y1 >> y2;

        int width = y1 - x1;
        int height = y2 - x2;

        for (int q = x1; q < y1; q++)
        {
            for (int w = x2; w < y2; w++)
            {
                matrix[q][w] = 1;
            }
        }
    }

    for (int i = 0; i < 100; i++)
    {
        for (int j = 0; j < 100; j++)
        {
            if (matrix[i][j] == 1)
            {
                result++;
            }
        }
    }

    cout << result << endl;
}