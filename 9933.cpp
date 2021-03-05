#include <iostream>
#include <string>
#include <algorithm>
#include <vector>

using namespace std;

pair<int, char> check(vector<string> v)
{
    int cnt;
    char alp;
    for (int i = 0; i < v.size(); i++)
    {
        string temp;
        temp = v[i];
        reverse(temp.begin(), temp.end());

        for (int j = i; j < v.size(); j++)
        {
            if (v[i].length() == v[j].length())
            {
                if (temp == v[j])
                {
                    cnt = v[j].length();
                    alp = v[j][v[j].length() / 2];
                }
            }
        }
    }
    pair<int, char> mypair = make_pair(cnt, alp);

    return mypair;
}

int main()
{
    int N;
    string word;
    vector<string> v;
    pair<int, char> p;

    cin >> N;
    for (int i = 0; i < N; i++)
    {
        cin >> word;
        v.push_back(word);
    }
    p = check(v);
    cout << p.first << " " << p.second << '\n';
}