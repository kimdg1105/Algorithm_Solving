#include <iostream>
#include <math.h>
using namespace std;

bool isPrime(int n)
{
    if (n == 1)
        return false;
    if (n == 2)
        return true;
    if (n % 2 == 0)
        return false;
    int rootnum = sqrt(n);
    for (int i = 3; i <= rootnum; i++)
    {
        if (n % i == 0)
        {
            return false;
        }
    }
    return true;
}

int *goldbach(int arr[], int num)
{
    int origin = num;
    int second = 0;
    int halfnum = num / 2;
    if (isPrime(halfnum))
    {
        arr[0] = halfnum;
        arr[1] = halfnum;
        return arr;
    }

    while (1)
    {
        halfnum--;
        if (isPrime(halfnum))
        {
            second = origin - halfnum;
            if (isPrime(second))
            {
                arr[0] = halfnum;
                arr[1] = second;
                break;
            }
        }
    }
    return arr;
}

int main()
{
    int T;
    cin >> T;
    int sample = 0;
    bool flag;
    int arr[2] = {};
    for (int i = 0; i < T; i++)
    {
        cin >> sample;
        goldbach(arr, sample);
        cout << arr[0] << " " << arr[1] << endl;
    }
    return 0;
}
