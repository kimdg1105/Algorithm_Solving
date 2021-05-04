#include <iostream>
using namespace std;

int main()
{
    int N;

    cin >> N;
    for (int i = 2; N > 0;)
    {
        if (N % i == 0)
        {
            N = N / i;
            cout << i << endl;
        }
        else
        {
            i++;
        }
        if (N == 1)
        {
            break;
        }
    }

    return 0;
}