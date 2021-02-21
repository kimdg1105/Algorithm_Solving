#include <iostream>
#define MAX 1001
using namespace std;

int main()
{
    int a, b;
    cin >> a >> b;

    int arr[1001] = {0};
    int idx = 1;

    for (int i = 1;; i++)
    {
        for (int j = 0; j < i; j++)
        {
            arr[idx++] = i;
            if (idx == MAX)
            {
                break;
            }
        }
        if (idx == MAX)
        {
            break;
        }
    }
    int sum = 0;
    for (int i = a; i <= b; i++)
    {
        sum += arr[i];
    }
    cout << sum;
}