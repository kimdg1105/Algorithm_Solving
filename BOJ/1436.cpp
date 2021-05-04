#include <iostream>
#include <algorithm>
#include <string>
#include <vector>

using namespace std;

int main()
{
    vector<int> v;
    int start = 666;
    string st_num;
    int N;
    cin >> N;
    v.push_back(start);

    int idx = 1;
    while (1)
    {
        start++;
        st_num = to_string(start);
        if (st_num.find("666") != -1)
        {
            int num = stoi(st_num);
            v.push_back(num);
            idx++;
        }
        if (idx == N)
        {
            break;
        }
    }

    cout << v[N - 1] << endl;
}