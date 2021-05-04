#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

#define MIN 987654321

int s[21][21] = {
    0,
};
bool flag[21] = {false};
int ans = MIN;
int N;
int member;

void dfs(int cur, int cnt)
{
    if (cnt == member)
    {
        vector<int> start, link;

        for (int i = 0; i < N; i++)
        {
            if (flag[i])
            {
                start.push_back(i);
            }
            else
            {
                link.push_back(i);
            }
        }
        int stat_start = 0, stat_link = 0;

        for (int i = 0; i < start.size(); i++)
        {
            for (int j = i + 1; j < start.size(); j++)
            {
                stat_start += s[start[i]][start[j]] + s[start[j]][start[i]];
                stat_link += s[link[i]][link[j]] + s[link[j]][link[i]];
            }
        }

        ans = min(ans, abs(stat_start - stat_link));
        return;
    }

    for (int i = cur + 1; i < N; i++)
    {
        if (flag[i] == false)
        {
            flag[i] = true;
            dfs(i, cnt + 1);
            flag[i] = false;
        }
    }
}

int main()
{

    cin >> N;
    member = N / 2;

    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            cin >> s[i][j];
        }
    }

    dfs(0, 0);
    cout << ans << '\n';
}