#include <iostream>
#include <vector>
#include <string>
#include <utility>

using namespace std;

int main()
{
    typedef pair<int, string> pp;
    typedef pair<int, pp> p;

    int N;
    vector<p> v;

    cin >> N;
    int age;
    string name;
    for (int i = 0; i < N; i++)
    {
        cin >> age >> name;
        pp mypp = make_pair(age, name);
        p myp = make_pair(i, mypp);
        v.push_back(myp);
    }

    for (int i = 0; i < v.size(); i++)
    {
        for (int j = i + 1; j < v.size(); j++)
        {
            if (v[i].second.first > v[j].second.first)
            {
                pp temp;
                temp = v[i];
                v[i] = v[j];
                v[j] = temp;
            }
        }
    }
    for (int i = 0; i < v.size(); i++)
    {
        for (int j = i + 1; j < v.size(); j++)
        {

            if (v[i].second.first == v[j].second.first)
            {
                if (v[i].first > v[j].first)
                {
                    p temp;
                    temp = v[i];
                    v[i] = v[j];
                    v[j] = temp;
                }
            }
        }
    }

    for (int i = 0; i < v.size(); i++)
    {
        cout << v[i].second.first << " " << v[i].second.second << '\n';
    }
}