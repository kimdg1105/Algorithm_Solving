#include <iostream>
#include <string>
#include <vector>

using namespace std;

void angle(int M, int N, int U, int L, int R, int D, vector<string> p)
{
    int width, height;
    int current = 1;
    vector<char> result;

    width = N + L + R;
    height = M + U + D;

    for (int i = 0; i < U; i++)
    {
        if (i % 2 != 0)
        {
            for (int j = 0; j < width; j++)
            {
                if (j % 2 != 0)
                {
                    result.push_back('#');
                }
                else
                {
                    result.push_back('.');
                }
            }
        }
        else
        {
            for (int j = 0; j < width; j++)
            {
                if (j % 2 != 0)
                {
                    result.push_back('.');
                }
                else
                {
                    result.push_back('#');
                }
            }
        }
        current++;
    }

    // middle
    int line = 0;
    for (int i = 0; i < M; i++)
    {
        if (current % 2 != 0)
        {
            for (int j = 0; j < L; j++)
            {
                if (j % 2 == 0)
                {
                    result.push_back('#');
                }
                else
                {
                    result.push_back('.');
                }
            }
            for (int k = 0; k < N; k++)
            {
                result.push_back(p[line][k]);
            }
            for (int j = 0; j < R; j++)
            {

                if (j % 2 == 0)
                {
                    result.push_back(result[L + N]);
                }
                else
                {
                    result.push_back(result[L + N - 1]);
                }
            }
            line++;

            current++;
        }
        else
        {
            for (int j = 0; j < L; j++)
            {
                if (j % 2 == 0)
                {
                    result.push_back('.');
                }
                else
                {
                    result.push_back('#');
                }
            }
            for (int k = 0; k < N; k++)
            {
                result.push_back(p[line][k]);
            }

            for (int j = 0; j < R; j++)
            {
                if (j % 2 == 0)
                {
                    result.push_back(result[L + N - 1]);
                }
                else
                {
                    result.push_back(result[L + N]);
                }
            }
            line++;

            current++;
        }
    }

    // bottom
    for (int i = 0; i < D; i++)
    {
        if (current % 2 == 0)
        {
            for (int j = 0; j < width; j++)
            {
                if (j % 2 != 0)
                {
                    result.push_back('#');
                }
                else
                {
                    result.push_back('.');
                }
            }
        }
        else
        {
            for (int j = 0; j < width; j++)
            {
                if (j % 2 != 0)
                {
                    result.push_back('.');
                }
                else
                {
                    result.push_back('#');
                }
            }
        }
        current++;
    }

    for (int i = 0; i < result.size(); i++)
    {
        cout << result[i];
        if ((i + 1) % width == 0)
        {
            cout << "\n";
        }
    }
}

int main()
{
    int M, N;
    int U, L, R, D;

    cin >> M >> N;
    cin >> U >> L >> R >> D;

    vector<string> puzzle;
    string word;

    for (int i = 0; i < M; i++)
    {
        cin >> word;
        puzzle.push_back(word);
    }
    angle(M, N, U, L, R, D, puzzle);
    return 0;
}
