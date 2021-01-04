#include <iostream>
#include <cstdlib>

using namespace std;

bool isprime(int n)
{
    int i = 2;
    while (1)
    {
        if (i == n)
        {
            return true;
        }
        if (n % i != 0)
        {
            i++;
        }
        else
        {
            return false;
        }
    }
}

int main()
{
    int T;
    int num;
    int base;
    int next = 0;
    int chai1, chai2;

    cin >> T;

    for (int i = 0; i < T; i++)
    {
        cin >> num;
        base = 3;
        while (1)
        {
            chai2 = chai1;
            next = num - base;
            if (isprime(base) && isprime(next))
            {
                chai1 = abs(base - next);
                if (chai1 < chai2)
                {
                    cout << base << ' ' << next << ' ' << chai1 << endl;
                    break;
                }
            }
            base += 1;

            // else
            // {
            //     base += 1;
            // }
        }
    }
    return 0;
}