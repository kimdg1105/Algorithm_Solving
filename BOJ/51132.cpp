#include <cstdio>

int main()
{
    int N;
    scanf("%d", &N);

    int star = N;
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < star; j++)
        {
            printf("*");
        }
        printf("\n");
    }
}