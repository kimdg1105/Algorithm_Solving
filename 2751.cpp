#include <stdio.h>
#include <algorithm>
#define MAX 10000000
using namespace std;

int main()
{
    int n;
    scanf("%d", &n);

    int arr[n];

    for (int i = 0; i < n; i++)
    {
        scanf("%d", &arr[i]);
    }
    sort(arr, arr + n);

    for (int i = 0; i < n; i++)
    {
        printf("%d\n", arr[i]);
    }
}