#include <cstdio>

int main()
{
    int N;
    scanf("%d", &N);

    int star = 1;
    int space = N - star;
    int middle = 1;
    bool start;
    bool flag = false;
    bool end = false;

    for (int cnt = 0; cnt < N; cnt++)
    {
        if (cnt == N - 1)
        {
            end = true;
        }
        if (cnt == 0)
        {
            for (int i = 0; i < space; i++)
            {
                printf(" ");
            }

            printf("*\n");
            space--;
        }

        else
        {
            if (start)
            {
                for (int i = 0; i < star; i++)
                {
                    printf("*\n");
                }
                start = false;
            }

            else
            {
                if (end)
                {
                    for (int i = 0; i < middle + 2 * star; i++)
                    {
                        printf("*");
                    }
                }
                else
                {
                    for (int i = 0; i < space; i++)
                    {
                        printf(" ");
                    }
                    for (int i = 0; i < star; i++)
                    {
                        printf("*");
                    }
                    for (int i = 0; i < middle; i++)
                    {
                        printf(" ");
                    }
                    for (int i = 0; i < star; i++)
                    {
                        printf("*\n");
                    }
                    middle += 2;
                    space--;
                }
            }
        }
    }
}