#include <iostream>
#include <unordered_map>
#include <vector>
#include <string>

using namespace std;

int main()
{
    int N;
    cin >> N;
    unordered_map<string, int> in;
    vector<string> outV;
    string car;

    for (int i = 1; i <= N; i++)
    {
        cin >> car;
        in.insert(make_pair(car, i));
    }
    for (int i = 1; i <= N; i++)
    {
        cin >> car;
        outV.push_back(car);
    }

    int cnt = 0;
    for (int i = 0; i < N; i++)
    {
        for (int j = i + 1; j < N; j++)
        {
            if (in[outV[i]] > in[outV[j]])
            {
                cnt++;
                break;
            }
        }
    }

    cout << cnt << endl;
}