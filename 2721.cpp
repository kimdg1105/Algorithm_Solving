#include <iostream>
using namespace std;

int calT(int n)
{
    int t = 0;
    for (int i = 1; i <= n; i++)
    {
        t += i;
    }
    return t;
}

int main()
{
    int n;
    int t = 0;

    int T;
    cin >> T;
    for (int i = 0; i < T; i++)
    {
        int w = 0;
        cin >> n;
        for (int k = 1; k <= n; k++)
        {
            w += k * calT(k + 1);
        }

        cout << w << '\n';
    }
}