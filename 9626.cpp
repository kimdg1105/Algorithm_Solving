#include <iostream>
#include <cstring>
#include <string>

#include <vector>

using namespace std;

char chess[20][20];

void make_chess(int width, int height)
{
    char start, next;

    for (int i = 0; i < height; i++)
    {
        if (i % 2 != 0)
        {
            start = '.';
            next = '#';
        }
        else
        {
            start = '#';
            next = '.';
        }
        for (int j = 0; j < width; j++)
        {
            chess[i][j] = start;
            char temp = start;
            start = next;
            next = temp;
        }
    }
}

int main()
{
    int M, N, U, L, R, D;

    cin >> M >> N;
    cin >> U >> L >> R >> D;

    int width = N + L + R;
    int height = M + U + D;
    char puzzle[M + 1][N + 1];
    for (int i = 0; i < M; i++)
    {
        for (int j = 0; j < N; j++)
        {
            cin >> puzzle[i][j];
        }
    }
    make_chess(width, height);

    for (int i = 0; i < M; i++)
    {
        for (int j = 0; j < N; j++)
        {
            chess[i + U][j + L] = puzzle[i][j];
        }
    }

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            cout << chess[i][j];
        }
        cout << '\n';
    }
}