#include <cstdio>

int main()
{
    int n;
    scanf("%d", &n);

    int reverse = 0;
    reverse = n - 1;

    int star = 1;
    int white = n - star;
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < star; j++)
        {
            printf("*");
        }
        // for (int j = 0; j < white; j++)
        // {
        //     printf(" ");
        // }
        // white--;
        star++;
        printf("\n");
    }
    // white = 1;

    star = n - 1;
    for (int i = 0; i < reverse; i++)
    {
        // for (int j = 0; j < white; j++)
        // {
        //     printf(" ");
        // }
        for (int j = 0; j < star; j++)
        {
            printf("*");
        }
        // white++;
        star--;
        printf("\n");
    }
}