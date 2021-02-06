#include <iostream>
#include <string>
#include <vector>

using namespace std;

bool isEyfa(string a, string b, int M)
{

    int cnt = 0;
    int idx = 0;

    for (int i = 0; i < a.size(); i++)
    {

        for (int j = 0; j < 2; j++)
        {
            if (a[i] == b[j + idx])
            {
                cnt++;
                // cout << "pass" << cnt << "\n";
            }
        }
        idx += 2;
    }
    if (cnt == 2 * M)
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
    int N, M;
    cin >> N >> M;

    vector<string> sample;
    vector<string> expand;
    string line;

    for (int i = 0; i < N; i++)
    {
        cin >> line;
        sample.push_back(line);
    }
    for (int i = 0; i < N; i++)
    {
        cin >> line;
        expand.push_back(line);
    }

    bool flag = false;
    for (int i = 0; i < N; i++)
    {
        flag = isEyfa(sample[i], expand[i], M);
        if (!flag)
        {
            cout << "Not Eyfa\n";
            return 0;
        }
    }
    if (flag)
    {
        cout << "Eyfa\n";
    }
}