#include <cstdio>

int main()
{
    int n;
    scanf("%d", &n);

    int star;
    star = n;
    int space = star - 1;
    bool odd = true;
    for (int i = 0; i < n; i++)
    {
        if (odd)
        {
            odd = false;
        }
        else
        {
            printf(" ");
            odd = true;
        }
        for (int j = 0; j < star; j++)
        {
            printf("*");
            if (space > 0)
            {
                printf(" ");
                space--;
            }
        }
        printf("\n");
        space = star - 1;
    }
}