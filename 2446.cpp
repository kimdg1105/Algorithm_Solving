#include <cstdio>

int main()
{
    int N;
    scanf("%d", &N);

    int star = 2 * N - 1;
    int white = 0;

    for (int i = 0; i <= 2 * N - 1; i++)
    {
        if (i < N)
        {
            for (int j = 0; j < white; j++)
            {
                printf(" ");
            }
            for (int j = 0; j < star; j++)
            {
                printf("*");
            }
            printf("\n");
            star -= 2;
            white += 1;
        }
        else if (i == N)
        {
            star += 2;
            white--;
        }
        else
        {
            white--;
            star += 2;
            for (int j = 0; j < white; j++)
            {
                printf(" ");
            }
            for (int j = 0; j < star; j++)
            {
                printf("*");
            }
            printf("\n");
        }
    }
}