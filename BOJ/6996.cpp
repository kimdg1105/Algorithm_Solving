#include <iostream>
#include <string>

using namespace std;

int main()
{
    int n;
    cin >> n;

    int sec_length;

    for (int i = 0; i < n; i++)
    {
        string first, second;
        cin >> first;
        string temp = first;
        cin >> second;
        int cnt = 0;
        if (first.size() != second.size())
        {
            cout << temp << " & " << second << " are NOT anagrams.\n";
        }
        else
        {
            for (int j = 0; j < second.size(); j++)
            {
                for (int k = 0; k < first.size(); k++)
                {
                    if (second[j] == first[k])
                    {
                        cnt++;
                        first[k] = '\0';
                        break;
                    }
                }
            }
            if (cnt == second.size())
            {
                cout << temp << " & " << second << " are anagrams.\n";
            }
            else
            {
                cout << temp << " & " << second << " are NOT anagrams.\n";
            }
            cnt = 0;
        }
    }
}