#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#define MAX 1000000000
using namespace std;

vector<int> op_cnt;
vector<char> op;
vector<string> comb;
vector<int> v;
int max_result = -MAX, min_result = MAX;

void make_comb()
{
    do
    {
        string st("");
        for (int i = 0; i < op.size(); i++)
        {
            st.push_back(op[i]);
        }
        comb.push_back(st);
    } while (next_permutation(op.begin(), op.end()));
}

void cal()
{
    int op_idx = 0;
    int num_idx = 0;
    for (int i = 0; i < comb.size(); i++)
    {
        string oper = comb[i];
        int sum = v[num_idx];
        for (int j = 0; j < oper.size(); j++)
        {
            num_idx++;
            if (oper[j] == '+')
            {
                sum = sum + v[num_idx];
            }
            else if (oper[j] == '-')
            {
                sum = sum - v[num_idx];
            }
            else if (oper[j] == '*')
            {
                sum = sum * v[num_idx];
            }
            if (oper[j] == '/')
            {
                if (sum < 0)
                {
                    sum = -(int)(abs(sum) / v[num_idx]);
                }
                else
                {
                    sum = (int)(sum / v[num_idx]);
                }
            }
        }
        if (sum > max_result)
        {
            max_result = sum;
        }
        if (sum < min_result)
        {
            min_result = sum;
        }
        num_idx = 0;
        sum = v[num_idx];
    }
    return;
}

int main()
{
    int N, num;

    cin >> N;

    for (int i = 0; i < N; i++)
    {
        cin >> num;
        v.push_back(num);
    }

    int cnt;
    for (int i = 0; i < 4; i++)
    {
        cin >> cnt;
        op_cnt.push_back(cnt);
    }

    for (int i = 0; i < 4; i++)
    {
        while (op_cnt[i] != 0)
        {
            if (i == 0)
            {
                op.push_back('+');
            }
            else if (i == 1)
            {
                op.push_back('-');
            }
            else if (i == 2)
            {
                op.push_back('*');
            }
            else if (i == 3)
            {
                op.push_back('/');
            }
            op_cnt[i]--;
        }
    }

    sort(op.begin(), op.end());
    make_comb();

    cal();

    cout << max_result << '\n'
         << min_result << '\n';

    return 0;
}
