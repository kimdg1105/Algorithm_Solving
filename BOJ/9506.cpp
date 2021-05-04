#include <iostream>
#include <vector>
using namespace std;

vector<int> check(int n)
{
    vector<int> v;

    for (int i = 1; i < n; i++)
    {
        if (n % i == 0)
        {
            v.push_back(i);
        }
    }
    return v;
}

int main()
{
    int n;

    while (1)
    {
        cin >> n;
        if (n == -1)
        {
            break;
        }
        vector<int> v = check(n);
        int sum = 0;

        for (int i = 0; i < v.size(); i++)
        {
            sum += v[i];
        }

        if (sum == n)
        {
            cout << n << " = ";
            for (int i = 0; i < v.size(); i++)
            {
                if (i == v.size() - 1)
                {
                    cout << v[i];
                }
                else
                {
                    cout << v[i] << " + ";
                }
            }
            cout << '\n';
        }
        else
        {
            cout << n << " is NOT perfect." << endl;
        }
    }
}