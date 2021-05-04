#include <iostream>
#include <string>
#include <algorithm>
#include <vector>

using namespace std;

#define A 1
#define B 2
#define C 3

int main()
{
    int N;
    cin >> N;
    vector<string> mirror;

    string line;
    for (int i = 0; i < N; i++)
    {
        cin >> line;
        mirror.push_back(line);
    }
    int state;
    cin >> state;

    if (state == A)
    {
        for (int i = 0; i < mirror.size(); i++)
        {
            cout << mirror[i] << '\n';
        }
    }

    if (state == B)
    {
        for (int i = 0; i < mirror.size(); i++)
        {
            reverse(mirror[i].begin(), mirror[i].end());
            cout << mirror[i] << '\n';
        }
    }
    if (state == C)
    {
        for (int i = mirror.size() - 1; i >= 0; i--)
        {
            cout << mirror[i] << '\n';
        }
    }
}