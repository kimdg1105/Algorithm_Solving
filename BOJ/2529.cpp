#include <iostream>
#include <vector>
using namespace std;

// void cal_max(char *oper, int k, vector<int> v)
// {
//     int start = 9;
//     int idx = 0;

//     while (1)
//     {
//         if (v.size() == k + 1)
//         {
//             break;
//         }
//         if (start > v[idx - 1] && oper[idx] == '>')
//         {
//             v.push_back(start);
//             start--;
//             idx++;
//         }
//         if (start < v[idx - 1] && oper[idx] == '<')
//         {
//             v.push_back(start);
//         }
//     }
// }

int main()
{
    int k;
    cin >> k;
    vector<int> max_v;
    vector<int> min_v;
    int start = 9;

    char oper[k + 1];

    for (int i = 0; i < k; i++)
    {
        cin >> oper[i];
    }

    //cal_max(oper, k, max_v);

    if (9 > max_v[0])
    {
        cout << "ji";
    }
    else
    {
        cout << "no";
    }
}
