#include <iostream>
using namespace std;

bool isCard(long card)
{
    //parse
    int arr[16] = {0};
    int idx = 15;
    int sum = 0;
    while (card > 0)
    {
        arr[idx] = card % 10;
        card /= 10;
        idx--;
    }

    for (int i = 14; i >= 0; i -= 2)
    {
        arr[i] = arr[i] * 2;
        if (arr[i] >= 10)
        {
            int f, s;
            s = arr[i] % 10;
            arr[i] /= 10;
            f = arr[i] % 10;
            arr[i] = f + s;
        }
    }

    for (int i = 0; i < 16; i++)
    {
        sum += arr[i];
    }

    if (sum % 10 == 0)
    {
        return true;
    }
    else
    {
        return false;
    }
}

int main()
{
    int n;
    cin >> n;

    long card;
    for (int i = 0; i < n; i++)
    {
        cin >> card;
        if (isCard(card))
        {
            cout << "T" << endl;
        }
        else
        {
            cout << "F" << endl;
        }
    }
}