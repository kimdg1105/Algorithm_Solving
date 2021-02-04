#include <iostream>
#include <cstdio>
using namespace std;

int main()
{
    int N;
    int star = 1;
    int white = 0;
    int idx = 0;
    cin >> N;
    white = 2 * N - 2 * star;
    for (int i = 0; i < 2 * N - 1; i++)
    {
        if (idx < N - 1)
        {
            for (int j = 0; j < star; j++)
            {
                printf("*");
            }
            for (int j = 0; j < white; j++)
            {
                printf(" ");
            }
            for (int k = 0; k < star; k++)
            {
                printf("*");
            }
            printf("\n");
            star++;
            idx++;
        }
        else
        {

            white = 2 * N - 2 * star;
            for (int k = 0; k < star; k++)
            {
                printf("*");
            }
            for (int j = 0; j < white; j++)
            {
                printf(" ");
            }
            for (int k = 0; k < star; k++)
            {
                printf("*");
            }
            printf("\n");
            star--;
        }
        white = 2 * N - 2 * star;
    }
}