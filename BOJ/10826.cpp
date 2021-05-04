#include <iostream>
#include <cstring>
#include <string>
#include <algorithm>

using namespace std;

string sum(string a, string b)
{
    int carry = 0;
    string result;

    while (!a.empty() | !b.empty() || carry)
    {
        if (!a.empty())
        {
            carry += a.back() - '0';
            a.pop_back();
        }
        if (!b.empty())
        {
            carry += b.back() - '0';
            b.pop_back();
        }
        result.push_back((carry % 10) + '0');
        carry /= 10;
    }
    reverse(result.begin(), result.end());
    return result;
}

string fibo(int N)
{
    string f, s, temp;
    f = "1";
    s = "1";
    if (N == 0)
    {
        return "0";
    }
    if (N == 1)
    {
        return s;
    }
    else
    {
        for (int i = 0; i < N - 2; i++)
        {
            temp = sum(f, s);
            f = s;
            s = temp;
        }
    }
    return s;
}

int main()
{
    int N;
    cin >> N;

    cout << fibo(N) << endl;
}