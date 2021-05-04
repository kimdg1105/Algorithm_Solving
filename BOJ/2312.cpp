#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

bool isPrime(int n)
{
    if (n == 1)
    {
        return false;
    }
    if (n == 2)
    {
        return true;
    }
    if (n % 2 == 0)
    {
        return false;
    }
    for (int i = 3; i < sqrt(n); i++)
    {
        if (n % i == 0)
        {
            return false;
        }
    }
    return true;
}

int main()
{
    int T;
    int N;

    cin >> T;
    for (int i = 0; i < T; i++)
    {
        vector<pair<int, int> > v;
        cin >> N;
        int cnt = 0;
        int start = 2;
        while (N != 1)
        {

            while (N % start == 0)
            {
                cnt++;
                N /= start;
            }
            v.push_back(make_pair(start, cnt));
            cnt = 0;
            while (1)
            {
                start++;
                if (isPrime(start))
                {
                    break;
                }
            }
        }
        for (int i = 0; i < v.size(); i++)
        {
            if (v[i].second != 0)
            {
                cout << v[i].first << " " << v[i].second << "\n";
            }
        }
    }
}