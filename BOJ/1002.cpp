#include <iostream>
#include <cmath>
using namespace std;

int main()
{
    int x1, y1, r1, x2, y2, r2;
    int T;
    double d;

    cin >> T;
    for (int i = 0; i < T; i++)
    {
        cin >> x1 >> y1 >> r1 >> x2 >> y2 >> r2;
        d = sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2));
        if (r1 > r2)
        {
            int temp = r2;
            r2 = r1;
            r1 = temp;
        } // sort

        if (r1 + r2 > d)
        {
            if (r2 - r1 < d)
            {
                cout << 2 << endl;
            }
        }

        if (r1 + r2 == d || r2 - r1 == d)
        {
            if (d == 0 && r1 == r2)
            {
                cout << -1 << endl;
            }
            else
            {
                cout << 1 << endl;
            }
        }

        if (r1 + r2 < d || d < r2 - r1)
        {
            cout << 0 << endl;
        }
    }

    return 0;
}