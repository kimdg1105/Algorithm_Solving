#include <iostream>
#include <cstring>

using namespace std;

int main()
{
    int n;
    cin >> n;

    char name[n + 1];
    for (int i = 0; i < n; i++)
    {
        cin >> name[i];
    }

    char alphabet[26] = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'};
    int score = 0;
    for (int i = 0; i < n; i++)
    {
        // cout << name[i] << " ";
        for (int j = 0; j < 26; j++)
        {
            if (name[i] == alphabet[j])
            {
                score += j + 1;
            }
        }
    }
    cout << score << endl;
}