#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

bool compare(string a, string b)
{
    if (a.length() == b.length())
    {
        return b.length() < 0;
    }
    return a.length() < b.length();
}

int main()
{
    int n;
    scanf("%d", &n);
    vector<string> wordvec;
    string word;
    for (int i = 0; i < n; i++)
    {
        cin >> word;
        if (find(wordvec.begin(), wordvec.end(), word) == wordvec.end())
        {
            wordvec.push_back(word);
        }
    }
    sort(wordvec.begin(), wordvec.end(), compare);
    for (int i = 0; i < wordvec.size(); i++)
    {
        printf("%s\n", wordvec[i].c_str());
    }
}