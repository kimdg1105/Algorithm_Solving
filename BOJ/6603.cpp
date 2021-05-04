#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

vector<int> lotto;

void nCr(int n, int r)
{
    if (r > n)
    {
        return;
    }
    vector<int> mask;

    for (int i = 0; i < n; i++)
    {
        if (i < r)
        {
            mask.push_back(0);
        }
        else
        {
            mask.push_back(1);
        }
    }

    sort(mask.begin(), mask.end());

    while (1)
    {
        for (int i = 0; i < n; i++)
        {
            if (mask[i] == 0)
            {
                cout << lotto[i] << " ";
            }
        }
        cout << '\n';
        if (!next_permutation(mask.begin(), mask.end()))
        {
            break;
        }
    }
    cout << '\n';
    lotto.clear();
}

int main()
{

    int k;

    while (1)
    {
        cin >> k;
        if (k == 0)
        {
            break;
        }
        else
        {
            int num;
            for (int i = 0; i < k; i++)
            {
                cin >> num;
                lotto.push_back(num);
            }
            nCr(k, 6);
        }
    }
}