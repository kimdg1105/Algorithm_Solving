#include <iostream>
using namespace std;

unsigned long long factorial(int n)
{
    unsigned long long total = 1;
    while (1)
    {
        if (n == 1)
        {
            break;
        }
        total *= n;
        n--;
    }
    return total;
}

int main()
{
    int n;
    cin >> n;

    unsigned long long f;
    f = factorial(n);
    cout << f << '\n';
}